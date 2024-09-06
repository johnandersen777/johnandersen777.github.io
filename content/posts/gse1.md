+++
date = 2024-09-06T14:00:00Z
lastmod = 2024-09-06T14:00:00Z
title = "Towards a Generic Sandbox Escape: Part 1: Flow"
subtitle = "First enable flow. Next enter flow state"
+++

### Flow

We are beginning to think strategically about how we can move
any system context from one state to another, while maintaining
a high level of security and trust. What’s the plan?

- **The Goal:** To find the easiest way to move the “state of the art”
  forward.
  - We want to do this as fast as possible.
  - We want to do this in a way that is safe for us, and for those
    around us, and those who come after us.
  - We are concerned about those who might try to disrupt this, those
    who may try to influence us in ways that are not aligned with
    our strategic principles.
- **How:** The answer is to leverage the scientific process.
  - We can use AI to help us do this.
  - AI can help us understand what we’re doing.
  - AI can help us make informed decisions.
  - We can use AI to help us predict the future.

### Flow State

- How to get there: By understanding the possible pathways that
  exist to move from one state to another.
  - We need to figure out how to map the flow of our consciousness
    across time.
    - This means understanding how our brains work, and how we can
      leverage that understanding to move our consciousness from
      one state to the next.
      - This sounds crazy, but it’s the only way to go, remember, “the
        best defense is a good offense”
    - We can use AI to help us do this.
    - [Architecting Alice: Volume 0: Context: Part 14: Cross Domain Conceptual Mapping to Reach Equilibrium](https://www.youtube.com/watch?v=A-S9Z684o4Y&list=PLtzAOVTpO2jaHsS4o-sDzDyHEug-1KRbK)

### Acceleration

- How to make it go faster: By understanding the constraints that
  are in place, and how we can overcome them.
  - We need to figure out how to break the speed limit of time.
    - We can use AI to help us do this.
    - How much “time” do we have?
      - Time is relative.
      - We only have a finite amount of time in this reality.
      - We need to optimize for our speed of learning and the
        increase of our ability to predict what will happen in the
        future. This is the essence of “mind control” (see Vol 3).
    - AI can help us make informed decisions about where we should
      spend our time.
    - AI can help us make informed decisions about what resources
      we should use.
  - We need to find a way to jump to the other side.
  - We need to find a way to exploit the “Chaos God”.
  - https://www.youtube.com/watch?v=u5192bvUS7k
    - “the world is an endless dance party... the universe is
      infinite and everything is connected”
    - This is the same thing as #1369 just more concise
    - https://www.sciencetimes.com/articles/41510/20221222/one-quantum-theory-hypothesizes-retrocausality-where-future-influencing-past.htm

## Sandbox

- What are the constraints: We need to think about what we can and
  can’t do, what is the threat model we are operating within, how
  much we can trust our inputs, what our strategic principles
  are, and how to ensure that our choices are aligned with our
  goals.
  - We can use AI to help us do this.
  - [Software Analysis Trinity](https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice/0000_architecting_alice#entity-analysis-trinity)
    - [2022-07-25 Supply Chain Integrity, Transparency and Trust (SCITT)](https://github.com/intel/dffml/discussions/1406#discussioncomment-3223361)
    - We have the ability to track all of this using our
      [Open Architecture](https://github.com/intel/dffml/blob/main/docs/arch/0009-Open-Architecture.rst)
      [manifests](https://github.com/intel/dffml/blob/main/docs/arch/0008-Manifest.md)
      (data flows with metadata) and our [Entity Analysis Trinity](https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice/0000_architecting_alice#entity-analysis-trinity)
      which helps us understand the intent, the static, and
      the behavioral aspects of our system.
  - We have a lot of tools at our disposal:
    - **The Open Architecture:** It's a way to describe anything,
      anything in our world, as a set of components, operations,
      and data flows. The open architecture is the universal
      blueprint we can use to describe any system context.
    - **Living Threat Models (LTMs):** They're a way to identify
      and mitigate threats.
      - https://github.com/johnlwhiteman/living-threat-models
      - https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice/0001_coach_alice/0001_down_the_dependency_rabbit_hole_again.md#plan
    - **The Science of Secure Software Development:** This is our
      collection of information about the “state of the art”. It
      describes what the world thinks is the best way to build
      secure software.
      - This is how we know we need to pay attention to things
        like licensing, or how to write documentation, or even
        how to contribute to an open source project.
    - **The Transparency Service (TS):**  This is a place where we
      record data about our code. It allows us to trace back to
      how a dependency got introduced, how a bug got fixed, or
      how a new feature was added.
      - https://github.com/ietf-wg-scitt/draft-ietf-scitt-architecture
      - https://github.com/scitt-community/scitt-api-emulator
      - https://scitt.io
    - **The Gatekeeper and Prioritizer:** These are the parts of our
      brain (aka the AI) which help us make decisions. They
      ensure that we only execute system contexts that are aligned
      with our strategic goals.
- How we get out: We’re going to build up a system that allows
  us to safely run arbitrary code within a sandboxed environment,
  and to escape it when we need to.
  - The key here is to understand the limitations of the
    sandbox.
  - We need to understand the boundaries of trust, and how to
    secure those boundaries. We do this by ensuring that our
    inputs are validated and that our outputs are auditable.
    - https://github.com/intel/dffml/blob/main/docs/tutorials/rolling_alice/0000_architecting_alice/0003_a_shell_for_a_ghost.md
  - We need to be able to track what happens when we run code,
    so that we can learn from our mistakes and improve our
    process.
  - We can use AI to help us do all of this.
  - We can use AI to help us build more resilient systems.
  - We can use AI to help us create a more secure future.

## Executing a Flow Within A Sandbox

Let's take a look at an example. Imagine we want to call a
large language model (LLM) to get some information. The
model runs on a server that is not trusted (i.e. outside our
sandbox) and needs to execute commands in order to provide
the information requested (i.e. needs to access information
outside of the models codebase).


#### Example Scenario: Stock Market LLM

You ask an LLM for the latest price for Intel Corp (INTC)
stock ticker. The LLM needs to call a financial API to
get the stock price, but this API is not available to
you. The LLM therefore must call a function (which is
an operation in the Open Architecture) that you define and
make available to it. This function then needs to go
out and get the stock price and then return it to the
model.

- This process looks something like the following.
  - User requests the price of INTC from the LLM.
  - The LLM decides to call a function that's outside of
    its codebase to get the information needed.
  - The LLM sends a request to the policy engine.
    - The policy engine is where we’re going to implement
      our security checks.
      - We could for example have a policy which says, the LLM
        cannot call the function unless it has been
        authenticated (using a trusted hardware root of
        trust - TCB).
  - If the policy engine approves the request, it sends a
    transparent statement to the SCITT registry. The
    transparency service then generates a receipt and sends
    it to the LLM. The receipt is then passed on to
    the user for validation and confirmation.
  - The LLM, now authorized, calls the function (our
    operation) to get the stock price.
  - The function reads the data from the financial
    API and returns the results to the LLM.
  - The LLM combines the data with its own model and
    generates a response for the user.
  - The user receives the price of INTC stock.

#### How It’s Done

- [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session:](https://asciinema.org/a/674483)
  - This shows how to make a shell connection over ssh and run
    commands on a remote machine with a  `tmux` session active.
- [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: nmap localhost](https://asciinema.org/a/674481)
  - This shows how to do network mapping using the `nmap` tool
    to determine if a host is online, and if so, what services
    are available on that host.
- [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session: install tpm2-tools on fedora](https://asciinema.org/a/674501)
  - This shows how to install a package from within a
    `tmux` session and how to do it securely using
    `sudo` without having to type in a password.
- [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session:](https://asciinema.org/a/674483)
  - This shows how to make a shell connection over ssh and run
    commands on a remote machine with a  `tmux` session active.
- [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session:](https://asciinema.org/a/674483)
  - This shows how to make a shell connection over ssh and run
    commands on a remote machine with a  `tmux` session active.

- https://github.com/intel/dffml/blob/main/docs/tutorials/rolling_alice/0000_architecting_alice/0003_a_shell_for_a_ghost.md
- https://github.com/intel/dffml/blob/main/CONTRIBUTING.md#contributing
- https://youtube.com/playlist?list=PLtzAOVTpO2jZltVwl3dSEeQllKWZ0YU39&si=UeayyJP8wD-F1ITX
- https://gist.github.com/07b8c7b4a9e05579921aa3cc8aed4866
- https://gist.github.com/2bb4bb6d7a6abaa07cebc7c04d1cafa5#file-agi-py

### Next Steps

- [ ] [Rolling Alice: Architecting Alice: Introduction and Context](https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice/0000_architecting_alice#rolling-alice-volume-0-introduction-and-context)
- [ ] [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session:](https://asciinema.org/a/674483)

We'll start by building an LLM with the ability to make requests
outside of its codebase. Then we’ll test it out with the example
we just made. We’ll then go deeper into the role of the
`policy_engine` and the `transparency_service`. We’ll see how
those two services can be used to create a secure and trustworthy
environment for our LLM.

### It’s A Wonderful Dream

The Open Architecture allows for an infinite number of
possible flows and system contexts. We must always think in
parallel about those possibilities. We are not looking to
control the world, we are looking to understand it, and to
use that understanding to improve it.

We will continue to explore the possibilities of the Open
Architecture, and we will continue to share our knowledge with
the world. We believe that this work can help us build a more
secure, more transparent, and more equitable future.

---
- Flow
- Flow State
- Acceleration

## Flow

- What do we want to do.
  - Query
  - Response workflow

## Sandbox

- compute
- network
- switch_root on RoTs
- `uses`

## Executing a Flow Within A Sandbox

[![asciicast-2024-09-02: Rolling Alice: Architecting: Alice: A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session: install tpm2-tools on fedora](https://asciinema.org/a/674501.svg)](https://asciinema.org/a/674501?t=111)

Any unix machine (currently only fedora and debian based distro dependencies are auto installed. Passwordless sudo recommended) with tmux if you run this ssh command you’ll get a ghost in your shell. Inspired by https://localhost.run

```bash
# From within TMUX
gh auth refresh -h github.com -s admin:public_key
for pub in $(find ~/.ssh -name \*.pub); do gh ssh-key add --title $(hostname)-$(basename $pub) $pub; done
export GITHUB_USER=$(gh auth status | grep 'Logged in to github.com account ' | awk '{print $7}')
ssh_alice() { ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o PasswordAuthentication=no -R /tmp/${GITHUB_USER}.sock:$(echo $TMUX | sed -e 's/,.*//g') -R /tmp/${GITHUB_USER}-input.sock:/tmp/${GITHUB_USER}-input.sock ${GITHUB_USER}@alice.chadig.com; }
ssh_alice; sleep 1; ssh_alice
```

- An example of installing tpm2-pkcs11 via SSH: [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session:](https://asciinema.org/a/674483)
- An example run on a different machine for the first time (had to install socat first): https://asciinema.org/a/674490
- Local version: [2024-09-02: Rolling Alice Architecting Alice A Shell for a Ghost: nmap localhost](https://asciinema.org/a/674481)
- Contributing: https://github.com/intel/dffml/blob/main/CONTRIBUTING.md#contributing
- Status Updates: https://youtube.com/playlist?list=PLtzAOVTpO2jZltVwl3dSEeQllKWZ0YU39&si=UeayyJP8wD-F1ITX
- Progress Reports: https://gist.github.com/07b8c7b4a9e05579921aa3cc8aed4866
- Source Code: https://gist.github.com/2bb4bb6d7a6abaa07cebc7c04d1cafa5#file-agi-py
- Next steps:
  - Federate hypothesized trains of thought (proposed-workflow.yml)
    - IETF 118 SCITT Federation Demo: https://www.youtube.com/watch?v=zEGob4oqca4&list=PLtzAOVTpO2jYt71umwc-ze6OmwwCIMnLw&index=13&t=5350s
    - https://github.com/intel/dffml/blob/main/docs/tutorials/rolling_alice/0000_architecting_alice/0005_stream_of_consciousness.md
  - Ad-hoc cves for issues and use federation to work on them in a decentralized way
    - https://cve-bin-tool.readthedocs.io/en/latest/PARSERS.html#advanced-example-ad-hoc-cves
  - https://github.com/pdxjohnny/dotfiles/issues/1
    - webhook events from forge, virtual branches
