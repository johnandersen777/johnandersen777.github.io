+++
date = 2020-07-07T19:00:00Z
lastmod = 2020-07-07T19:00:00Z
title = "Time Saving Tricks and Hacks"
subtitle = ""
+++

## dos2unix in Python

Remove carrage returns from CRLF (carrage return, line feed: `\r\n`).

```console
$ python -c 'import pathlib, sys; p = pathlib.Path(sys.argv[-1]); p.write_bytes(p.read_bytes().replace(b"\r", b""))' file.txt
```

## Get list of available versions

```console
$ python -m pip install dffml==
```

## Download file with Python from command line with progress

```console
$ python3 -c 'import sys, functools, urllib.request; print(urllib.request.urlretrieve(sys.argv[-1], reporthook=lambda n, c, t: print(f"{round(((n*c)/t) * 100, 2)}%", end="\r", file=sys.stderr))[0])' https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps.zip
```

[![asciicast](https://asciinema.org/a/357044.svg)](https://asciinema.org/a/357044)

## Display only blocks of text with certain text in them

Use grep to displays blocks of text. Only display blocks with certain text
inside them.

```console
$ git grep -A 25 -E 'dffml train|dffml accuracy|dffml predict' | python -c 'import sys; print("--".join([i for i in sys.stdin.read().split("--") if not "model-directory" in i]).strip())'
```

## Display a file as plain text in a browser

```console
$ (echo -e 'HTTP/1.0 200 OK\n' && cat myfile.txt) | nc -Nlp 8080
```

Redisplay on reload.

- `-N` to netcat mean close socket on EOF from STDIN

```console
$ nodemon -e md --exec "clear; while test 1; do (echo -e 'HTTP/1.0 200 OK\n' && cat open-architecture.md) | nc -Nlp 8000; sleep 0.5; done; test 1"
```

## Do a vim commands on files in an automated way

Remove all newlines from end of file

```console
$ for file in $(echo examples/notebooks/*.ipynb); do vim -b '+set noeol' '+wq' $file; done
```

## Open a list of files in tmux panes

```console
$ for file in $(git ls-files | grep -E '.*\.cpp|.*\.h|.*\.ino'); do tmux split-window -h "vim ${file}"; tmux next-layout; done
```

[![asciicast](https://asciinema.org/a/441107.svg)](https://asciinema.org/a/441107)

## Close all but the active tmux pane

```console
$  for pane in $(tmux list-pane | grep -v active | sed -e 's/:.*//g'); do export pane=$(tmux list-pane | grep -v active | sed -e 's/:.*//g' | head -n 1); tmux kill-pane -t $pane ; done
```

## Scrape page for links

```console
$ curl -sfL "https://pypi.org/simple/dffml/" | python -u -c 'import sys, json, bs4; print(json.dumps({link.get_text(): link.get("href") for link in bs4.BeautifulSoup(sys.stdin.read(), "html.parser").find_all("a")}))' | python -m json.tool
{
    "dffml-0.4.0.post0-py3-none-any.whl": "https://files.pythonhosted.org/packages/37/d5/6dc945d453cbdeb15db4249fe09e07bdd2e750a6f256fd893c81ced7bbbb/dffml-0.4.0.post0-py3-none-any.whl#sha256=031dd3a4ca57d46f568f7dd2711a223a26bc343f5f2ac36e1af881ead19e05b6",
    "dffml-0.4.0.post0.tar.gz": "https://files.pythonhosted.org/packages/b0/42/a151555fe3b45926fa041813f8513d883180bdb9e8def64d2d5260609743/dffml-0.4.0.post0.tar.gz#sha256=f6f898c504450e3514dd5791b31bcba21ad9edfc3e896ac5da9cbe3181af5d2b"
}
```

## Sign and verify data using ssh keys

References:
- https://www.agwa.name/blog/post/ssh_signatures

```console
$ podman run -v $HOME/.ssh/:/root/.ssh:ro -v $PWD:/usr/src/workdir -w /usr/src/workdir --rm -ti --entrypoint ssh-keygen lscr.io/linuxserver/openssh-server -Y sign -f /root/.ssh/mykeyname -n file CHANGELOG.md
$ (printf 'alice@example.com ' && cat ~/.ssh/mykeyname.pub) | tee allowed_signers
$ cat CHANGELOG.md | podman run -v $HOME/.ssh/:/root/.ssh:ro -v $PWD:/usr/src/workdir -w /usr/src/workdir --rm -i --entrypoint ssh-keygen lscr.io/linuxserver/openssh-server -Y verify -f allowed_signers -I alice@example.com -n file -s CHANGELOG.md.sig
Good "file" signature for alice@example.com with RSA key SHA256:RQsUY/opy5KWg+pesXcjI9I3I1z8udgkFAlOjDrv8cw
```

## git stash show patch

Shows just applied patch

```console
$ git stash show -p
```


## wsl start sshd

From powershell:

```console
$ Start-Job -ScriptBlock{wsl -u root -e mkdir -pv /run/sshd ; wsl -u root -e /usr/sbin/sshd -D}
```

## WSL Forward Port

Run the following from an Administrator PowerShell session

```powershell
PS C:\WINDOWS\system32> netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2222 connectaddress=((wsl -u root -- sh -c "ip a | grep inet\ | grep -v 127.0.0").Split()[5].Split("/")[0]) connectport=22

PS C:\WINDOWS\system32> netsh advfirewall firewall add rule name="Open Port 2222 for WSL2" dir=in action=allow protocol=TCP localport=2222
Ok.

PS C:\WINDOWS\system32> netsh interface portproxy show v4tov4

Listen on ipv4:             Connect to ipv4:

Address         Port        Address         Port
--------------- ----------  --------------- ----------
0.0.0.0         2222        172.23.21.232   22
```

## GitHub CLI set secrets

**../secrets**

```
SECRET_NAME secret value
```

```console
$ while IFS= read -r line; do gh secret set -R github.com/intel/dffml "$(echo $line | sed -e 's/ .*//')" --body "$(echo $line | sed -e 's/[^ ]* //')"; done < ../secrets
```

## Return repos from sourcegraph query

```console
$ curl 'https://sourcegraph.com/search/stream?q=context%3Aglobal%20repo%3A%5Egithub%5C.com%2Forg-name%2F.*%20log4j%20&v=V2&t=literal&dl=0&dk=html&dc=1&display=1500' | tee /tmp/org-name
$ python -c 'import sys, json, itertools; print("\n".join(list(set(filter(bool, itertools.chain(*map(lambda data: list(map(lambda content: content.get("repository", ""), data)) if isinstance(data, list) else [], filter(bool, map(json.loads, map(lambda line: "{}" if not line.startswith("data: ") else line.split(maxsplit=1)[-1], sys.stdin))))))))))' < /tmp/org-name
```

## Commit one file at a time

```console
$ git add $(git status --porcelain=2 | grep -v \? | awk '{print $NF}' | head -n 1) && git commit -sm "$(git status --porcelain=2 | grep -v \? | awk '{print $NF}' | sed -e 's/dffml_source_mongodb\///g' -e 's/examples\/shouldi\///g' -e 's/\//: /g' -e 's/_/ /g' -e 's/\.py//g' | head -n 1): Format with black"
```

## Run command on line in vim

Source: https://stackoverflow.com/questions/26809543/how-to-use-an-external-command-in-vim-to-modify-the-selection

```
How to use an external command in Vim to modify the selection

Something I've found useful in other editors is the ability to:

take the selected text
run an external command and pass the selection to its stdin
take the external commands stdout and replace the current selection with it.
This way you can write useful text tools which operate on the selection using any language that can do basic io.

How can this be done with vim?

(Directly in the command line, or via a key binding?)

---

:'<,'>!command

'<,'> represents the (linewise) visual selection and is automatically inserted when you hit : and have something selected.

Example:

If you select a line containing:

print("Hello!")

and run the Vim command:

:'<,'>!python

the text will be replaced with Hello!.

If you want to set this to a key-binding (F5 to evaluate for example)

vnoremap <F5> :!python<cr>
```

## Dump GitHub comments to markdown file

```console
$ gh issue view https://github.com/intel/dffml/issues/1279 --json comments | jq -r '.comments[].body' | tr -d '\r' | sed -e 's/[[:space:]]*$//' -e 's/^#/\n\n#/g' | tee ~/comments.$(date "+%4Y-%m-%d-%H-%M").md
```

## Print the date in a YYYY-MM-DD-HH-SS format

```console
$ date "+%Y-%m-%d-%H-%M"
2022-02-02-06-34
```

## Reproducable archive via ssh

Source: https://reproducible-builds.org/docs/archives/

```console
$ tar -C /some/dir/with/stuff -c --sort=name --mtime="2015-10-21 00:00Z" --owner=0 --group=0 --numeric-owner --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime myfile.within.some.dir.with.stuff.exe | sshpass -p "$(python -m keyring get $USER password)" ssh -o StrictHostKeyChecking=no "$USER@129.168.1.123" python -c '
import io
import os
import sys
import tarfile
import hashlib
import pathlib
import unittest
import tempfile

artifacts_contents = sys.stdin.buffer.read()

unittest.TestCase().assertEqual(
    hashlib.sha256(artifacts_contents).hexdigest(),
    "2bd972e3c980ee7dd376ca2c5988e2234d325d505f2124146abad226f1d163bb",
    "Artifact archive hash mismatch",
)

with tempfile.TemporaryDirectory() as tempdir:
    os.chdir(tempdir)
    with tarfile.open(fileobj=io.BytesIO(artifacts_contents), mode="r") as fileobj:
        fileobj.extractall()
        for path in pathlib.Path().rglob("*"):
            print(path.resolve())
'
```

## Converting datetimes from one timezone to another in Python

Example has local timezone as `-08:00` (PST).

```python
>>> from datetime import datetime, timedelta, tzinfo
>>> (datetime.fromisoformat('2022-02-13T04:30') + timedelta(hours=28)).isoformat() + "-08:00"
'2022-02-14T08:30:00-08:00'
>>> (datetime.fromisoformat('2022-02-13T04:30') + timedelta(hours=28) + timedelta(hours=8) + timedelta(hours=5, minutes=30)).isoformat() + "+05:30"
'2022-02-14T22:00:00+05:30'
```

## XZ compressed asciinema recording

Dotfiles: https://github.com/pdxjohnny/dotfiles/blob/cae7a366d7766bb1a82c478f0aedc6a829630677/.asciinema_source

Record

```console
$ python -m asciinema rec --idle-time-limit 0.5 --title "$(date +%4Y-%m-%d-%H-%M)" --command "sh -c 'tmux a || tmux'" >(xz --stdout - > "$HOME/Downloads/asciinema-rec-$(date +%4Y-%m-%d-%H-%M).json.xz")
```

Check size

```console
du -h ~/Downloads/ascii*
```

Playback

```console
xz --stdout -d - < ~/Downloads/asci* | python -m asciinema play -s 20 -
```

## OBS Studio

https://snoober.home.blog/

## wsl ssh

```console
$ wsl -u root -- mkdir -pv /run/sshd; wsl -u root -- /usr/sbin/sshd -D -o ListenAddress=0.0.0.0
```

## Parse time with timezone

```console
$ python -c 'import sys, datetime; print(datetime.datetime.strptime(sys.argv[-1], "%d %b %Y %H:%M:%S %z"))' '11 Jan 2022 00:44:19 +0800'
2022-01-11 00:44:19+08:00
```

## date command

```console
$ date "+%4Y-%m-%d-%H-%M"
```

## File transfer with progress

Machine sending file.

```console
$ nc -Nlp 9999 < filename
```

Machine receiveing file.

```console
$ dd status=progress bs=1M if=<(cat < /dev/tcp/example.com/9999) of=/mnt/c/Users/$USER/Downloads/filename
```

## Work on one branch and make change on other branch push to github and run CI

```console
$ nodemon -e yml --exec "clear; export branch=feedface; git branch -D $branch; git checkout upstream/main-test -b $branch; python -c 'print(\"A\" + (\"R\" * (2**8)))' > ahoy-there-matey-its-me-file; git add . && git commit -sam "${branch}" && git push -d origin "${branch}"; git push -fu origin $(git status | head -n 1 | awk '{print $NF}') && gh pr create --base main-test --title "$branch" -F /dev/null"
```

## Download and install an autotools project with a vendored `autoreconf -i`

```console
$ export tempdir=$(mktemp -d); (cd $tempdir && curl -sfL 'https://www.kernel.org/pub/software/scm/git/git-2.36.0.tar.gz' | tar xz && cd git* && ./configure --prefix=$tempdir && make -j $(($(nproc)*4)) && ./git version && echo $tempdir | tee /tmp/git_pwd && sudo chmod a+rx -R $tempdir) && sudo chmod a+r /tmp/git_pwd
```

A non autoconf project using https://www.gnu.org/prep/standards/html_node/Directory-Variables.html#Directory-Variables for
`prefix      ?= /usr/local`

```console
$ export tempdir=$(mktemp -d); (cd $tempdir && curl -sfL https://github.com/stefanhaustein/TerminalImageViewer/archive/refs/tags/v1.1.1.tar.gz | tar xz && cd Terminal*/src/main/cpp && make -j $(($(nproc)*4)) && make install prefix=$tempdir)
install -D tiv /tmp/tmp.ONSIPt2W5E/bin/tiv
```

## Near local github actions debug

```console
$ gh run rerun --failed $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}')
$ gh run watch --exit-status -i 1 $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}')
$ gh run view $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}')
$ gh run view --log $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}')
```

## Find the binaries

**TODO** CVE Bin Tool approach

```console
$ file $(find $tempdir -name git)
/tmp/tmp.2Wd0hLb8oN/bin/git:                                      ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c1357c209d816a9738b0af78d017a6c2bfba71e7, with debug_info, not stripped
/tmp/tmp.2Wd0hLb8oN/git-2.36.0/bin-wrappers/git:                  POSIX shell script, ASCII text executable
/tmp/tmp.2Wd0hLb8oN/git-2.36.0/git:                               ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c1357c209d816a9738b0af78d017a6c2bfba71e7, with debug_info, not stripped
/tmp/tmp.2Wd0hLb8oN/git-2.36.0/contrib/mw-to-git/bin-wrapper/git: POSIX shell script, ASCII text executable
/tmp/tmp.2Wd0hLb8oN/libexec/git-core/git:                         ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c1357c209d816a9738b0af78d017a6c2bfba71e7, with debug_info, not stripped
```

## UNIX anyone can execute and read anything in these dirs

```console
$ chmod -R a+rx $dir
```

## Debugging actions self-hosted runners

```console
$ gh run rerun --failed $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}') && sleep 1 && gh run watch --exit-status -i 1 $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}') || gh run view --log $(gh run list | head -n 2 | tail -n 1 | awk '{print $(NF-2)}')
```

## Used the menu button on the keyboard for the first time ever today

https://support.google.com/chrome/answer/10483214?hl=en

## Edit a file only if autoformating passes

Can be used to hand edit xxd as well if you wanted to

```console
$ cp old-admin.json old-old-admin.json; cp ~/.local/admin.json old-admin.json && python -m json.tool old-admin.json > admin.json || cp old-admin.json admin.json && cp admin.json staged.json && vim staged.json && python -m json.tool < staged.json > admin.json && cp admin.json ~/.local/admin.json
```
