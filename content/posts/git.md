+++
date = 2021-07-16T16:00:00Z
lastmod = 2021-07-16T16:00:00Z
author = "default"
title = "Git"
subtitle = "Git usage tips and tricks"
+++


## Rebase bulk rename commit messages

```console
git filter-branch --msg-filter 'sed "s/Refs: #xxxxx/Refs: #22917/g"' master..my_branch
```

> https://stackoverflow.com/questions/14332551/whats-the-fastest-way-to-edit-hundreds-of-git-commit-messages

## Configure git to rebase on pull instead of merge

```console
git config --global pull.rebase true
```

## Arange patch files by date

```python
"""
Arange patch files given as args and outputs the patch files ordered by the date
within the patch file.
"""
import sys
import pathlib
import argparse
import datetime
import itertools


def make_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "patches",
        type=pathlib.Path,
        nargs="+",
        help="The .patch files to organize by date",
    )
    return parser


def main(args):
    parser = make_parser()
    args = parser.parse_args(args)
    patches = itertools.chain(
        *[
            [
                (
                    patch,
                    datetime.datetime.strptime(
                        line.split(maxsplit=1)[-1],
                        "%a, %d %b %Y %H:%M:%S %z",
                    ),
                )
                for line in patch_contents
                if line.startswith("Date:")
            ]
            for patch, patch_contents in [
                (patch, patch.read_text(errors="ignore").split("\n"))
                for patch in args.patches
            ]
        ]
    )
    for patch, date in sorted(patches, key=lambda i: i[1]):
        print(str(patch), date)


if __name__ == "__main__":
    main(sys.argv)
```

## Branching

We support multiple branches so as to provide stability to our users.
If they go write some code based off our last release, and then we
release, and no longer support the last version, they will have to
turn around right after they implemented and update all their code to
use our new APIs. If we support at least two versions, then it gives
people time to do other things than spend all their time updating to
the lastest version of our libraries API!
