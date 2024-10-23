+++
date = 2021-01-23T06:00:00Z
lastmod = 2021-01-23T06:00:00Z
author = "default"
title = "Digital Ocean Python Scripting"
subtitle = "Automating Application Deployment and Load Balancing on Digital Ocean"
+++

This post is some heavily commented example code that shows you how you can use
Python to script up creation of Digital Ocean VMs (Droplets), start web servers
on them, and connect them to a load balancer that provides TLS (LB coming
in an update to this post later).

The code for do.py can be found here:
https://gist.github.com/johnandersen777/f1f13d77dc7dd4403a6647baa3926042

The first time we'll see that there are no containers to kill or remove. And
that the Python 3.8 container had to be pulled down before it could be run.

```console
$ DIGITALOCEAN_ACCESS_TOKEN=20b7f300f7d84b752c11239c568c81b3bc010cb49026968f19d3a84deeaa6baa python do.py
{'my-test-app-sfo2-s-1vcpu-1gb-1': <Droplet: 227830340 my-test-app-sfo2-s-1vcpu-1gb-1>, 'my-test-app-sfo2-s-1vcpu-1gb-0': <Droplet: 227830027 my-test-app-sfo2-s-1vcpu-1gb-0>}
[178.128.7.222] [err]   "docker kill" requires at least 1 argument.
[178.128.7.222] [err]   See 'docker kill --help'.
[178.128.7.222] [err]
[178.128.7.222] [err]   Usage:  docker kill [OPTIONS] CONTAINER [CONTAINER...]
[178.128.7.222] [err]
[178.128.7.222] [err]   Kill one or more running containers
[167.99.96.5]   [err]   "docker kill" requires at least 1 argument.
[167.99.96.5]   [err]   See 'docker kill --help'.
[167.99.96.5]   [err]
[167.99.96.5]   [err]   Usage:  docker kill [OPTIONS] CONTAINER [CONTAINER...]
[167.99.96.5]   [err]
[167.99.96.5]   [err]   Kill one or more running containers
[178.128.7.222] [err]   "docker rm" requires at least 1 argument.
[178.128.7.222] [err]   See 'docker rm --help'.
[178.128.7.222] [err]
[178.128.7.222] [err]   Usage:  docker rm [OPTIONS] CONTAINER [CONTAINER...]
[178.128.7.222] [err]
[178.128.7.222] [err]   Remove one or more containers
[167.99.96.5]   [err]   "docker rm" requires at least 1 argument.
[167.99.96.5]   [err]   See 'docker rm --help'.
[167.99.96.5]   [err]
[167.99.96.5]   [err]   Usage:  docker rm [OPTIONS] CONTAINER [CONTAINER...]
[167.99.96.5]   [err]
[167.99.96.5]   [err]   Remove one or more containers
[167.99.96.5]   3172daa1cf000bc0dbce3ba912cfb18358b38481cccbb7585f01c6c1f87389f4
[167.99.96.5]   [err]   Unable to find image 'python:3.8' locally
[167.99.96.5]   [err]   3.8: Pulling from library/python
[167.99.96.5]   [err]   b9a857cbf04d: Pulling fs layer
[167.99.96.5]   [err]   d557ee20540b: Pulling fs layer
[167.99.96.5]   [err]   3b9ca4f00c2e: Pulling fs layer
[167.99.96.5]   [err]   667fd949ed93: Pulling fs layer
[167.99.96.5]   [err]   4ad46e8a18e5: Pulling fs layer
[167.99.96.5]   [err]   381aea9d4031: Pulling fs layer
[167.99.96.5]   [err]   8a9e78e1993b: Pulling fs layer
[167.99.96.5]   [err]   9eff4cbaa677: Pulling fs layer
[167.99.96.5]   [err]   1addfed3cc19: Pulling fs layer
[167.99.96.5]   [err]   667fd949ed93: Waiting
[167.99.96.5]   [err]   4ad46e8a18e5: Waiting
[167.99.96.5]   [err]   381aea9d4031: Waiting
[167.99.96.5]   [err]   8a9e78e1993b: Waiting
[167.99.96.5]   [err]   9eff4cbaa677: Waiting
[167.99.96.5]   [err]   1addfed3cc19: Waiting
[167.99.96.5]   [err]   d557ee20540b: Verifying Checksum
[167.99.96.5]   [err]   d557ee20540b: Download complete
[167.99.96.5]   [err]   3b9ca4f00c2e: Verifying Checksum
[167.99.96.5]   [err]   3b9ca4f00c2e: Download complete
[167.99.96.5]   [err]   b9a857cbf04d: Verifying Checksum
[167.99.96.5]   [err]   b9a857cbf04d: Download complete
[167.99.96.5]   [err]   381aea9d4031: Verifying Checksum
[167.99.96.5]   [err]   381aea9d4031: Download complete
[167.99.96.5]   [err]   667fd949ed93: Verifying Checksum
[167.99.96.5]   [err]   667fd949ed93: Download complete
[167.99.96.5]   [err]   8a9e78e1993b: Verifying Checksum
[167.99.96.5]   [err]   8a9e78e1993b: Download complete
[167.99.96.5]   [err]   9eff4cbaa677: Verifying Checksum
[167.99.96.5]   [err]   9eff4cbaa677: Download complete
[167.99.96.5]   [err]   1addfed3cc19: Verifying Checksum
[167.99.96.5]   [err]   1addfed3cc19: Download complete
[167.99.96.5]   [err]   4ad46e8a18e5: Verifying Checksum
[167.99.96.5]   [err]   4ad46e8a18e5: Download complete
[167.99.96.5]   [err]   b9a857cbf04d: Pull complete
[167.99.96.5]   [err]   d557ee20540b: Pull complete
[167.99.96.5]   [err]   3b9ca4f00c2e: Pull complete
[167.99.96.5]   [err]   667fd949ed93: Pull complete
[167.99.96.5]   [err]   4ad46e8a18e5: Pull complete
[167.99.96.5]   [err]   381aea9d4031: Pull complete
[167.99.96.5]   [err]   8a9e78e1993b: Pull complete
[167.99.96.5]   [err]   9eff4cbaa677: Pull complete
[167.99.96.5]   [err]   1addfed3cc19: Pull complete
[167.99.96.5]   [err]   Digest: sha256:fe08f4b7948acd9dae63f6de0871f79afa017dfad32d148770ff3a05d3c64363
[167.99.96.5]   [err]   Status: Downloaded newer image for python:3.8
[178.128.7.222] 54ae127c7abf3cd3d8f3b1cbe909c586c046c9d40fbb139c39b263ef72bd4df8
[178.128.7.222] [err]   Unable to find image 'python:3.8' locally
[178.128.7.222] [err]   3.8: Pulling from library/python
[178.128.7.222] [err]   b9a857cbf04d: Pulling fs layer
[178.128.7.222] [err]   d557ee20540b: Pulling fs layer
[178.128.7.222] [err]   3b9ca4f00c2e: Pulling fs layer
[178.128.7.222] [err]   667fd949ed93: Pulling fs layer
[178.128.7.222] [err]   4ad46e8a18e5: Pulling fs layer
[178.128.7.222] [err]   381aea9d4031: Pulling fs layer
[178.128.7.222] [err]   8a9e78e1993b: Pulling fs layer
[178.128.7.222] [err]   9eff4cbaa677: Pulling fs layer
[178.128.7.222] [err]   1addfed3cc19: Pulling fs layer
[178.128.7.222] [err]   667fd949ed93: Waiting
[178.128.7.222] [err]   4ad46e8a18e5: Waiting
[178.128.7.222] [err]   381aea9d4031: Waiting
[178.128.7.222] [err]   8a9e78e1993b: Waiting
[178.128.7.222] [err]   9eff4cbaa677: Waiting
[178.128.7.222] [err]   1addfed3cc19: Waiting
[178.128.7.222] [err]   d557ee20540b: Verifying Checksum
[178.128.7.222] [err]   d557ee20540b: Download complete
[178.128.7.222] [err]   3b9ca4f00c2e: Verifying Checksum
[178.128.7.222] [err]   3b9ca4f00c2e: Download complete
[178.128.7.222] [err]   b9a857cbf04d: Verifying Checksum
[178.128.7.222] [err]   b9a857cbf04d: Download complete
[178.128.7.222] [err]   381aea9d4031: Verifying Checksum
[178.128.7.222] [err]   381aea9d4031: Download complete
[178.128.7.222] [err]   667fd949ed93: Verifying Checksum
[178.128.7.222] [err]   667fd949ed93: Download complete
[178.128.7.222] [err]   8a9e78e1993b: Verifying Checksum
[178.128.7.222] [err]   8a9e78e1993b: Download complete
[178.128.7.222] [err]   9eff4cbaa677: Verifying Checksum
[178.128.7.222] [err]   9eff4cbaa677: Download complete
[178.128.7.222] [err]   1addfed3cc19: Verifying Checksum
[178.128.7.222] [err]   1addfed3cc19: Download complete
[178.128.7.222] [err]   4ad46e8a18e5: Verifying Checksum
[178.128.7.222] [err]   4ad46e8a18e5: Download complete
[178.128.7.222] [err]   b9a857cbf04d: Pull complete
[178.128.7.222] [err]   d557ee20540b: Pull complete
[178.128.7.222] [err]   3b9ca4f00c2e: Pull complete
[178.128.7.222] [err]   667fd949ed93: Pull complete
[178.128.7.222] [err]   4ad46e8a18e5: Pull complete
[178.128.7.222] [err]   381aea9d4031: Pull complete
[178.128.7.222] [err]   8a9e78e1993b: Pull complete
[178.128.7.222] [err]   9eff4cbaa677: Pull complete
[178.128.7.222] [err]   1addfed3cc19: Pull complete
[178.128.7.222] [err]   Digest: sha256:fe08f4b7948acd9dae63f6de0871f79afa017dfad32d148770ff3a05d3c64363
[178.128.7.222] [err]   Status: Downloaded newer image for python:3.8
[nodemon] clean exit - waiting for changes before restart
```

If we re-run we'll see that the `docker kill` and `docker rm` commands succeed
this time.

```console
$ DIGITALOCEAN_ACCESS_TOKEN=20b7f300f7d84b752c11239c568c81b3bc010cb49026968f19d3a84deeaa6baa python do.py
{'my-test-app-sfo2-s-1vcpu-1gb-1': <Droplet: 227830340 my-test-app-sfo2-s-1vcpu-1gb-1>, 'my-test-app-sfo2-s-1vcpu-1gb-0': <Droplet: 227830027 my-test-app-sfo2-s-1vcpu-1gb-0>}
SSH Private Key (/home/johnandersen777/.ssh/id_rsa) Password:
[178.128.7.222] 54ae127c7abf
[167.99.96.5]   3172daa1cf00
[178.128.7.222] 54ae127c7abf
[167.99.96.5]   3172daa1cf00
[178.128.7.222] 935710fd1ba64fe8b70ccd695a1f60c956e9712c7a36ba8d2e3f0dc87a1b01d9
[167.99.96.5]   27abd899ba5c19a0022c2bf633fe467c9d914e32d34d7264ada06810eede10b2
```

**TODO** Add load balancing with TLS
