+++
date = 2020-07-07T19:00:00Z
lastmod = 2020-07-07T19:00:00Z
title = "Time Saving Tricks and Hacks"
subtitle = ""
+++

## dos2unix in Python

Remove carrage returns from CRLF (carrage return, line feed: `\r\n`).

```consoele
$ python -c 'import pathlib, sys; p = pathlib.Path(sys.argv[-1]); p.write_bytes(p.read_bytes().replace(b"\r", b""))' file.txt
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
$ (echo -e 'HTTP/1.0 200 OK\n' && cat myfile.txt) | nc -lp 8080
```
