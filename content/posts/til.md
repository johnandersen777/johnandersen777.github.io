+++
date = 2021-01-09T16:00:00Z
lastmod = 2021-01-09T16:00:00Z
author = "default"
title = "Today I Learned"
subtitle = "Tips and tricks"
+++

# 2021-01-8

Forward a UNIX socket over SSH. This command will sit around in the background.

References: https://github.com/moby/moby/pull/18373#issuecomment-184895457

```console
$ ssh -L ./mysock:/var/run/docker.sock -Nf hostname.example.com
```

# 2021-01-09

https://stackoverflow.com/questions/65515652/fix-cannot-update-component-from-inside-function-body-of-different-component-w

Some thoughts:
Pretty sure it’s because we call setState within the render method, which is
whatever method returns JSX, `return (<stuff>...</stuff>)`.

I think it doesn’t like that since we pass the setter to the child, then the
child renders, and could immediately call setState (`if (data === true)`), which
triggers a re-render in the parent, which triggers a re-render in the child,
which calls setState... and causes an infinite loop effectively.

Create wrapper around setter and pass to children
https://github.com/intel/dffml/blob/b88424a927f6279191285e2103a2b50b993b1921/service/webui/webui/src/Paperbase.js#L167-L205
https://github.com/intel/dffml/blob/b88424a927f6279191285e2103a2b50b993b1921/service/webui/webui/src/Paperbase.js#L228-L236

Old style class accepting wrapped setter (props.saveBackend())
https://github.com/intel/dffml/blob/b88424a927f6279191285e2103a2b50b993b1921/service/webui/webui/src/SetBackendPopup.js#L16-L48

New style class accepting wrapped setter (saveBackend())
https://github.com/intel/dffml/blob/b88424a927f6279191285e2103a2b50b993b1921/service/webui/webui/src/SettingsBackend.js#L44-L60

# 2021-01-13

**TODO** Add notes about meetings and people skills stuff

# 2021-01-14

Split screen PC games!

https://www.reddit.com/r/nucleuscoop/comments/fjdqid/list_of_new_supported_games_and_faq/

# 2021-02-12

Sealed boxes, anonymously encrypt something using a public key

https://libsodium.gitbook.io/doc/public-key_cryptography/sealed_boxes

# 2021-02-17

Regular experssion builder helper

https://regex101.com/

# 2021-02-27

Inspect memory of running process

https://superuser.com/questions/231776/how-do-i-see-a-history-of-what-ive-post-ed-in-google-chrome/1119310#1119310

Hedge Fund Legend Paul Tudor Jones
"5:1 (risk /reward) Five to one means I’m risking one dollar to make five.  What five to one does is allow you to have a hit ratio of 20%.  I can actually be a complete imbecile. I can be wrong 80% of the time and I’m still not going to lose."

https://mobile.twitter.com/realwillmeade/status/1365661871999713283
