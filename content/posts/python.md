+++
title = "Python"
subtitle = "Python programming development guide and gotchas"
date = "2020-10-12T14:50:57-07:00"
lastmod = "2020-10-12T14:50:57-07:00"
+++

> This post is in progress

# `async def` and `await`

`await` is a keyword which means "give me the return value *when it's ready*".
The caller is understands the return value may not be ready right away. The
caller knows that the callee may not have the return value right away since the
callee function was defined with `async def`. Using the `await` keyword tells
Python that the caller wishes to pause execution (stay at the same line) and
wait for the callee's return value to be ready. Pausing of execution is usually
due to (but not limited to) network events, such as sending or receiving of
data, or the completion of work done within another thread or process.

The power of using `async def` (and
[`asyncio`](https://docs.python.org/3.7/library/asyncio-task.html) in general)
is that since the execution of a caller can be paused, multiple `async def`
functions can be run at the same time, an `async def` function is also known as
a coroutine. When a coroutine reaches the point where it would be waiting on an
event, such as completion of work in another thread or process, or a network
receive, etc. Python pauses the execution of that coroutine, and checks if there
is another coroutine that was waiting for an event which completed during the
running of the previous coroutine. If it finds a coroutine that was waiting for
a now complete event, it runs that coroutine until it either completes, or until
it is stuck waiting on another event.
