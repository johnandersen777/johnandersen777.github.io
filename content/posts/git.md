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
