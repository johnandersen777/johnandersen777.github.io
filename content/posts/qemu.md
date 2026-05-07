+++
date = 2020-07-24T06:00:00Z
lastmod = 2020-07-24T06:00:00Z
title = "QEMU"
subtitle = "QEMU Tips and Tricks"
+++

QEMU is an indispensable tool for the virtual machine inclined. It's a command
line utility for running virtual machines.

Main documentation: https://www.qemu.org/docs/master/system/


## Virtiofs

```bash
#!/usr/bin/env bash
set -xeuo pipefail

TEMPDIR="$(mktemp -d)"
trap "rm -rf ${TEMPDIR}" EXIT

# ── 1. Build chroot (unchanged) ────────────────────────────────────────────
if [[ ! -d my-chroot ]]; then
  mkdir -p temp_oci_layout my-chroot
  skopeo copy --format oci docker://registry.fedoraproject.org/fedora:latest dir:./temp_oci_layout/
  cat temp_oci_layout/manifest.json | jq -r '.layers[].digest' | sed -e 's/sha256://' \
    | xargs -I '{}' -- sudo tar -xzkf 'temp_oci_layout/{}' -C ./my-chroot

  sudo systemd-nspawn -D ./my-chroot dnf -y install \
    systemd kernel-core cloud-init \
    dracut dracut-live dracut-network \
    btrfs-progs util-linux rsyslog \
    openssh-server vim tmux
fi

# ── 2. Journald config (unchanged) ────────────────────────────────────────
sudo mkdir -p my-chroot/etc/systemd/journald.conf.d
sudo tee my-chroot/etc/systemd/journald.conf.d/serial.conf <<'EOF'
[Journal]
ForwardToConsole=yes
MaxLevelConsole=debug
EOF

# ── 3. Build initrd with dmsquash-live ────────────────────────────────────
if [[ ! -f my-chroot/boot/initrd.img ]]; then
  # Write a dracut.conf that includes the live modules
  sudo tee my-chroot/etc/dracut.conf.d/live.conf <<'EOF'
add_dracutmodules+=" dmsquash-live "
filesystems+=" squashfs overlay ext4 "
compress="zstd"
hostonly="no"
EOF

  KVER=$(ls my-chroot/lib/modules/ | tail -1)
  sudo systemd-nspawn -D ./my-chroot \
    dracut --force /boot/initrd.img "$KVER"

  sudo chown "${USER}:${USER}" my-chroot/boot/initrd.img
fi

# ── 4. Build squashfs image ───────────────────────────────────────────────
# dracut dmsquash-live looks for /LiveOS/squashfs.img on the root= device.
# We'll put it in a staging dir that virtiofsd will serve.
if [[ ! -f liveos/LiveOS/squashfs.img ]]; then
  mkdir -p liveos/LiveOS
  # Exclude the virtual fs mount points and the squashfs dir itself
  sudo mksquashfs my-chroot liveos/LiveOS/squashfs.img \
    -comp zstd \
    -e my-chroot/proc \
    -e my-chroot/sys \
    -e my-chroot/dev \
    -e my-chroot/run \
    -noappend
fi

# Build squashfs into a disk image that QEMU can present as a block device
if [[ ! -f liveos.img ]]; then
  mkdir -p liveos-staging/LiveOS

  sudo mksquashfs my-chroot liveos-staging/LiveOS/squashfs.img \
    -comp zstd \
    -e my-chroot/proc \
    -e my-chroot/sys \
    -e my-chroot/dev \
    -e my-chroot/run \
    -noappend

  # Size the image to fit + some headroom
  SQSIZE=$(du -sb liveos-staging/LiveOS/squashfs.img | cut -f1)
  # Add 15% headroom for ext4 metadata and journal
  IMGSIZE=$(( SQSIZE * 115 / 100 ))
  # Round up to nearest MB
  IMGSIZE=$(( (IMGSIZE + 1048575) / 1048576 * 1048576 ))
  truncate -s "$IMGSIZE" liveos.img

  # Format as ext4 and copy in the LiveOS layout
  mkfs.ext4 -L LIVEOS liveos.img
  mkdir -p /tmp/liveos-mnt
  sudo mount -o loop liveos.img /tmp/liveos-mnt
  sudo mkdir -p /tmp/liveos-mnt/LiveOS
  sudo cp liveos-staging/LiveOS/squashfs.img /tmp/liveos-mnt/LiveOS/squashfs.img
  sudo umount /tmp/liveos-mnt
fi

# ── 5. virtiofsd serving the LiveOS directory ─────────────────────────────
VIRTIOFS_SOCKET="/tmp/vfs-$(uuidgen).sock"
/usr/libexec/virtiofsd \
  --socket-path="$VIRTIOFS_SOCKET" \
  --shared-dir="${PWD}/liveos" \
  --cache always \
  --readonly \
  --sandbox none &
VFS_PID=$!
trap 'kill $VFS_PID; rm -f "$VIRTIOFS_SOCKET"' EXIT

# ── 6. cloud-init (unchanged) ─────────────────────────────────────────────
cat <<EOF > user-data
#cloud-config
users:
  - name: agent
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
chpasswd:
  expire: False
  users:
  - name: agent
    password: agent
    type: text
EOF
cat <<EOF > meta-data
instance-id: someid/somehostname
EOF
touch vendor-data

python -um http.server --directory . 0 2>&1 > "${TEMPDIR}/listening.txt" &
CLOUD_INIT_HTTPD_PID=$!
trap 'kill $CLOUD_INIT_HTTPD_PID' EXIT
until grep http "${TEMPDIR}/listening.txt"; do sleep 0.1; done
PORT=$(cat "${TEMPDIR}/listening.txt" | awk '{print $6}')

# ── 7. Boot ───────────────────────────────────────────────────────────────
KVER=$(ls my-chroot/lib/modules/ | tail -1)
KERNEL=$(find my-chroot/usr/lib/modules -name vmlinuz)


qemu-system-x86_64 \
  -net nic \
  -net user \
  -smbios type=1,serial=ds="nocloud;s=http://10.0.2.2:${PORT}/" \
  -no-reboot \
  -enable-kvm \
  -cpu host \
  -smp cpus=2 \
  -m 4G \
  -nographic \
  -initrd "${PWD}/my-chroot/boot/initrd.img" \
  -kernel "${PWD}/${KERNEL}" \
  -drive file=liveos.img,format=raw,if=virtio,readonly=on \
  -append "console=ttyS0 \
    root=live:LABEL=LIVEOS \
    rd.live.image \
    rd.overlayfs=1 \
    rd.live.overlay.overlayfs=1 \
    init=/usr/lib/systemd/systemd"

```

## Example Flags

Run a 64 bit Intel / AMD system

```console
qemu-system-x86_64 ...
```

### KVM

Without KVM your VM will be VERY VERY VERY slow. You'll want to enable this.

```
  -enable-kvm
```

Make sure your use account has access to `/dev/kvm`, use `chown` to make the
group `kvm`, and add your user to that group. You'll need log out and log back
in for changes to take effect. Or run `bash --login`.

```console
$ groupadd kvm
$ sudo usermod -aG kvm $USER
$ ll /dev/kvm
crw-rw-rw- 1 root root 10, 232 Jul 22 12:10 /dev/kvm
$ chown root:kvm /dev/kvm
$ ll /dev/kvm
crw-rw-rw- 1 root kvm 10, 232 Jul 22 12:10 /dev/kvm
```

### Multiple CPUs

```
  -smp cpus=4
```

More detailed

```
  -smp sockets=1,cpus=4,cores=2 -cpu host
```

### Memory

```
  -m 8192M
```

### Networking - NAT

```
  -netdev user,id=mynet0 \
  -device virtio-net-pci,netdev=mynet0
```

You can also do what's known as "bridged" networking. It can be a bit of a mess
though. It's covered in the main QEMU documentation at the top.

> TODO Cover bridged networking

### USB

You may want to give a VM control over a USB device, such as a USB NIC.

Creating a ehci device and attaching the usb device to it is important!

Use `lsusb -v` to find the idProduct (productid) and idVendor (vendorid)

```
  -usb \
  -device usb-ehci,id=ehci \
  -device usb-host,bus=ehci.0,vendorid=0x0424,productid=0xEC00
```

### Share small files

```
  -virtfs local,path=$PWD/share,mount_tag=host0,security_model=mapped-file,id=host0
```

### Fast Random Number Generator

```
  -device virtio-rng-pci
```

### Port Forwarding

```
  -net \
    user,hostfwd=tcp::2222-:22,hostfwd=tcp::4444-:2222
```

### Guest Image

For a raw `.img` or `.iso`

```
  -drive \
    file="image.iso",if=virtio,aio=threads,format=raw
```

For a `.qcow2`

```
  -drive \
    file="image.qcow2",if=virtio,aio=threads,format=qcow2
```

### Kernel

Boot directly to a Linux kernel binary (skips some BIOS stuff)

```
  -kernel \
    "linux-source-tree/arch/x86/boot/bzImage"
```

### Kernel cmdline

The `root*` options here correspond to the
[Host Filesystem Passthrough](#host-filesystem-passthrough) section.

```
  -append \
    "console=ttyS0 rootfstype=9p root=fsdev-root ro rootflags=trans=virtio,version=9p2000.u init=/usr/lib/systemd/systemd"
```

### Disable GUI

```
  -nographic
```

### CPU Emulation

Specify `host` to have QEMU not emulate another CPU, just use the host CPU.

```
  -cpu host
```

### Specify BIOS

You'll need this if you want to use UEFI

```
  -bios \
    "path/to/OVMF.fd"
```

### BIOS Debugging Connection

```
  -chardev \
    pipe,path=qemudebugpipe,id=seabios \
  -device \
    isa-debugcon,iobase=0x402,chardev=seabios
```

Reference: https://www.seabios.org/Debugging#Debugging_with_gdb_on_QEMU

### Host Filesystem Passthrough

Use a directory on the host as a filesystem for the guest.

This requires that the guest kernel has been configured with:

```
CONFIG_9P_FS=y
CONFIG_9P_FS_POSIX_ACL=y
CONFIG_9P_FS_SECURITY=y
CONFIG_NET_9P=y
CONFIG_NET_9P_VIRTIO=y
```

*9P fs is buggy as all hell* In particular, fsync seems to be broken.

```
  -fsdev \
    local,id=fsdev-root,path="${CHROOT}",security_model=passthrough,readonly \
  -device \
    virtio-9p-pci,fsdev=fsdev-root,mount_tag=/dev/root
```

Make sure you're using the [corresponding kernel cmdline](#kernel-cmdline)
options.

### Creating A Bootable UEFI Guest Image

Create `qcow2` image

```console
$ qemu-img create -f qcow2 image.qcow2 20G
```

> Source of NBD commands: https://gist.github.com/shamil/62935d9b456a6f9877b5

Enable network block devices

```console
$ sudo modprobe nbd max_part=8
```

Map the image file to the `/dev/nbd0` network block device

```console
$ sudo qemu-nbd --connect=/dev/nbd0 image.qcow2
```

Create GPT partition table (UEFI)

```console
$ sudo parted /dev/nbd0 << 'EOF'
mklabel gpt
mkpart primary fat32 1MiB 261MiB
set 1 esp on
mkpart primary linux-swap 261MiB 10491MiB
mkpart primary ext4 10491MiB 100%
EOF
```

Format partitions

```console
$ sudo mkfs.fat /dev/nbd0p1
$ sudo mkswap /dev/nbd0p2
$ sudo mkfs.ext4 /dev/nbd0p3
```

Unmount and disconnect

```console
$ sudo umount -R /mnt/somepoint/
$ sudo qemu-nbd --disconnect /dev/nbd0
```

> parted commands from: https://wiki.archlinux.org/index.php/Parted#UEFI/GPT_examples

### CPU Hotplug

```conole
  -smp 1,maxcpus=2 -qmp unix:/tmp/q,server,nowait
```

In another shell

```console
$ sudo qemu/scripts/qmp/qmp-shell -p -v /tmp/q
Welcome to the QMP low-level shell!
Connected to QEMU 4.1.0

(QEMU) device_add id=cpu-2 driver=host-x86_64-cpu socket-id=1 core-id=0 thread-id=0 die-id=0
```

Back in your Linux guest you'll see
`[   51.190460] CPU1 has been hot-added` in the dmesg logs.

To initialize the CPU within the guest

```console
# echo 1 > /sys/devices/system/cpu/cpu1/online
```

> Reference: https://wiki.qemu.org/Features/CPUHotplug

### Precompiled UEFI Firmware

https://cdn.download.clearlinux.org/image/OVMF.fd

```
UEFI_BIOS="-bios OVMF.fd"

if [ -f OVMF_VARS.fd -a -f OVMF_CODE.fd ]; then
    UEFI_BIOS=" -drive file=OVMF_CODE.fd,if=pflash,format=raw,unit=0,readonly=on "
    UEFI_BIOS+=" -drive file=OVMF_VARS.fd,if=pflash,format=raw,unit=1 "
fi
```

## Links

1184122 – Can't mount virtio-9p fs at boot time
https://bugzilla.redhat.com/show_bug.cgi?id=1184122#c1

bootc-dev/bootc: Boot and upgrade via container images
https://github.com/bootc-dev/bootc

cloud-hypervisor/docs/vsock.md at main · cloud-hypervisor/cloud-hypervisor
https://github.com/cloud-hypervisor/cloud-hypervisor/blob/main/docs/vsock.md

dracut tries to mount virtiofs root before kernel has enumerated available virtiofs tags · Issue #22
https://github.com/dracut-ng/dracut-ng/issues/2242

dracut-ng/modules.d/71overlayfs-crypt/prepare-overlayfs-crypt.sh at e1bf57a772198becf126aebdfd2240ce
https://github.com/dracut-ng/dracut-ng/blob/e1bf57a772198becf126aebdfd2240cebc49b2f3/modules.d/71overlayfs-crypt/prepare-overlayfs-crypt.sh

DRACUT.CMDLINE(7) :: Dracut
https://dracut-ng.github.io/dracut-ng/man/dracut.cmdline.7.html

DRACUT(8) :: Dracut
https://dracut-ng.github.io/dracut-ng/man/dracut.8.html#using-the-dracut-shell

firecracker/docs/vsock.md at main · firecracker-microvm/firecracker
https://github.com/firecracker-microvm/firecracker/blob/main/docs/vsock.md

Getting Started with Bootable Containers :: Fedora Docs
https://docs.fedoraproject.org/en-US/bootc/getting-started/

hyperlight-dev/hyperlight-sandbox: A multi-backend sandboxing framework for running untrusted code w
https://github.com/hyperlight-dev/hyperlight-sandbox

hyperlight-dev/hyperlight: Hyperlight is a lightweight Virtual Machine Manager (VMM) designed to be 
https://github.com/hyperlight-dev/hyperlight

Invocation — QEMU documentation
https://qemu-project.gitlab.io/qemu/system/invocation.html#hxtool-6

Linux Kernel Development Tips And Tricks : Public Domain Relay
https://publicdomainrelay.com/linux-kernel/

linux/block/early-lookup.c at master · torvalds/linux
https://github.com/torvalds/linux/blob/master/block/early-lookup.c

linux/block/early-lookup.c at master · torvalds/linux
https://github.com/torvalds/linux/blob/master/block/early-lookup.c#L197

model-spec/docs/aikit.md at 783d1c84157ebde6c4014ac975d96c838cdee8f9 · modelpack/model-spec
https://github.com/modelpack/model-spec/blob/783d1c84157ebde6c4014ac975d96c838cdee8f9/docs/aikit.md

modelpack/model-spec at 783d1c84157ebde6c4014ac975d96c838cdee8f9
https://github.com/modelpack/model-spec/tree/783d1c84157ebde6c4014ac975d96c838cdee8f9

Post by @filippo.abyssdomain.expert — Bluesky
https://bsky.app/profile/filippo.abyssdomain.expert/post/3mkldvg6iec2h

skopeo/docs/skopeo-copy.1.md at main · containers/skopeo
https://github.com/containers/skopeo/blob/main/docs/skopeo-copy.1.md

ssh virtio systemd at DuckDuckGo
https://duckduckgo.com/?q=ssh+virtio+systemd&ia=web

sulogin(8) - Linux manual page
https://www.man7.org/linux/man-pages/man8/sulogin.8.html

sysroot.mount: About to execute: /usr/bin/mount virtfs:foo /sysroot -o ro · Issue #1397 · dracut-ng/
https://github.com/dracut-ng/dracut-ng/issues/1397

systemd-ssh-proxy
https://www.freedesktop.org/software/systemd/man/latest/systemd-ssh-proxy.html\

systemd-ssh-proxy(1) - Linux manual page
https://www.man7.org/linux/man-pages//man1/systemd-ssh-proxy.1.html

systemd-ssh-proxy(1) — Arch manual pages
https://man.archlinux.org/man/systemd-ssh-proxy.1.en

rpmfile for downloading kernel oob
https://github.com/srossross/rpmfile

The kernel’s command-line parameters — The Linux Kernel documentation
https://www.kernel.org/doc/html/v6.19/admin-guide/kernel-parameters.html

virtio-fs / virtiofsd · GitLab
https://gitlab.com/virtio-fs/virtiofsd

virtiofs - shared file system for virtual machines / Standalone usage
https://virtio-fs.gitlab.io/howto-qemu.html

virtiofs: virtio-fs host<->guest shared file system — The Linux Kernel documentation
https://www.kernel.org/doc/html/v6.19/filesystems/virtiofs.html

VM Interface
https://systemd.io/VM_INTERFACE/
