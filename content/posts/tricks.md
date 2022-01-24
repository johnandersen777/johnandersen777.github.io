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
$ (echo -e 'HTTP/1.0 200 OK\n' && cat myfile.txt) | nc -lp 8080
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
