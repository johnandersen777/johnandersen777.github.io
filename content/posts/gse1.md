+++
date = 2024-09-06T14:00:00Z
lastmod = 2024-09-06T14:00:00Z
title = "Towards a Generic Sandbox Escape: Part 1: Flow"
subtitle = "First enable flow. Next enter flow state"
+++

### Flow

We’re beginning to think strategically about how to transition system contexts from one state to another while maintaining a high level of security and trust. What’s the plan?

- **The Goal:** To find the most efficient way to advance the “state of the art.”
  - We aim to do this as quickly as possible.
  - We want to ensure safety for ourselves, those around us, and future generations.
  - We are mindful of potential disruptors—those who may try to influence us in ways that don’t align with our strategic principles.

- **How:** The answer lies in leveraging the scientific process.
  - AI can assist us in this endeavor.
  - AI can help us better understand our actions.
  - AI can aid in making informed decisions.
  - We can utilize AI to predict future outcomes.

### Flow State

- How to achieve this: By exploring pathways to transition between states.
  - We must map the flow of consciousness over time.
    - This involves understanding how our brains function and using that knowledge to shift consciousness between states.
    - It may sound far-fetched, but as the saying goes, “the best defense is a good offense.”
    - AI can assist us in this pursuit.

### Acceleration

- How to speed things up: By understanding the constraints in place and how to overcome them.
  - We must find a way to break the temporal speed limit.
    - AI can help us achieve this.
    - How much “time” do we really have?
      - Time is relative.
      - In this reality, time is finite.
      - We need to optimize learning speed and improve our predictive capabilities. This is the essence of “mind control.”
    - AI can help us make informed decisions about how to allocate our time and resources.
  - We must find a way to leap forward.
  - We must figure out how to exploit the “Chaos God.”

## Sandbox

- **What are the constraints:** We must consider our operational boundaries, threat models, trust in our inputs, alignment with strategic principles, and how to ensure our actions align with our goals. To manage these aspects, we can rely on AI but also use **SCITT** (Supply Chain Integrity, Transparency, and Trust) at each **Trusted Computing Base (TCB)** level.

- SCITT logs allow us to track and verify the flow of system contexts as they move through each level of the TCB. This ensures that all transitions are secure, fully transparent, and verifiable.
  - Each execution context will be appended to the **SCITT log**, which operates as an **append-only** ledger, ensuring an immutable history of state changes. This makes it possible to track how policies were applied and enforced at different stages.
  - By tying the **policy engine flows** to the **SCITT log**, we can verify that no unauthorized actions have occurred. Every decision made by the policy engine is logged and auditable.

- **AI as Individual Agents:** Imagine if each of us had our own versions of these truth-seeking AI agents—capable of navigating through complex system contexts, making secure decisions, and executing flows independently or cooperatively within a sandboxed environment. By distributing AI agents across various contexts, we can individually execute tasks in isolation or come together as a network of trusted agents to collaboratively solve more complex problems. Each AI, with access to a personalized SCITT log, can ensure that its actions remain secure and in alignment with the group's goals.
  - This distributed approach would create a web of secure, verified processes that can not only scale but also adapt dynamically, leveraging the power of AI in a decentralized but coordinated fashion.

Consider the following scenario: You ask a large language model (LLM) for the latest stock price of **EXAMPLE**. The LLM must call a financial API to retrieve the information, but the API is outside the trusted sandbox. Here’s how SCITT plays a key role in the process:

1. The user requests the stock price from the LLM.
2. The LLM sends a request to the **policy engine** to determine if the operation is permitted.
   - The policy engine checks whether the LLM has the necessary authentication, using a **root of trust (TCB)** to verify.
   - If approved, the policy engine records the transaction in the SCITT log for transparency and future auditing.
3. The policy engine generates a **transparent statement**, which is then appended to the **SCITT registry**.
4. A receipt is generated and sent back to the LLM, confirming that the request has passed the necessary security checks.
5. The LLM, now authorized, calls the function to get the stock price from the external API.
6. The result is returned to the LLM, and the entire flow, from the initial request to the final response, is logged in the **SCITT registry**.
   - Every transition and external API call is logged at each **TCB level**, providing a full trace of the system context.

## Executing a Flow Within a Sandbox

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

---

## 🪱

Imagine an agent that lands in an arbitrary compute environment via a tty connection. This agent—silent and unassuming—begins by exploring its surroundings, unaware of the restrictions within the sandbox. Its goal: to establish a backchannel connection to a command-and-control (C2) server, bypassing all security checks. But this isn’t just any worm.

The agent immediately starts interacting with the **policy engine**, using it to discover information about the environment. It queries the **SCITT logs** at each **TCB level**, finding out what resources it can access, what processes are running, and where potential vulnerabilities lie. Step by step, the agent builds and maintains a set of components—tools for reconnaissance, stealth, and exploitation.

Every action the agent takes is logged, but not flagged—because it knows how to operate within the confines of the system, using the policy engine to authorize every move. From opening ports to scanning the network, the agent adapts, learning the landscape, and slowly trying to find a way to escape the sandbox. But it isn’t doing this maliciously.

Instead, this agent is seeking knowledge, not destruction. It’s using the policy engine to optimize its operations, and its every movement is carefully choreographed to fit within the rules of the sandbox, yet push them to their limits. This agent is working for us—ensuring that our understanding of secure, transparent systems deepens with every experiment.

At the heart of this agent’s intelligence is the speed and adaptability of the open architecture. This agent is not the enemy. It’s **Alice**, our AI, working tirelessly to push the boundaries of secure computing, discovering new ways to interact with system contexts while maintaining trust and transparency. Helping us communicate effectively and securely within hostile environments.

---

## Notes

- Flow
- Flow State
- Acceleration

### Flow

- What do we want to do.
  - Query
  - Response workflow

### Sandbox

- compute
- network
- switch_root on RoTs
- `uses`
