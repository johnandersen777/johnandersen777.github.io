+++
date = 2024-09-06T14:00:00Z
lastmod = 2024-09-06T14:00:00Z
title = "Towards a Generic Methodology for Sandbox Escape: Part 1: Flow"
subtitle = "First enable flow. Next enter flow state"
+++

## Series

- [Flow](https://pdxjohnny.github.io/gse1/)
- [Flow State](https://pdxjohnny.github.io/gse2/)
- [Acceleration](https://pdxjohnny.github.io/gse3/)

## Context

- [DFFML: docs: tutorials: Rolling Alice](https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice)
- [Katherine Druckman - Threat Modeling Down the Rabbit Hole - OpenAtIntel](https://openatintel.podbean.com/e/threat-modeling-down-the-rabbit-hole/)
- [Gabe Cohen - On Decentralized Trust](https://decentralgabe.xyz/on-decentralized-trust/)
- [Harald Sack - Symbolic and Subsymbolic AI - An Epic Dilemma?](https://github.com/lysander07/Presentations/raw/main/EGC2023_Symbolic%20and%20Subsymbolic%20AI%20%20-%20an%20Epic%20Dilemma.pdf)
- [Nancy Eckert - Swarm Intelligence and Human Systems - BSides Portland 2019](https://youtu.be/Eq33S_Rz4qo?t=1117)
- [Robin Berjon - The Internet Transition](https://berjon.com/internet-transition/)
- [Adam Frank, David Grinspoon, and Sara Walker - Intelligence as a planetary scale process](https://www.cambridge.org/core/journals/international-journal-of-astrobiology/article/intelligence-as-a-planetary-scale-process/5077C784D7FAC55F96072F7A7772C5E5)

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

## Sandbox

![knowledge-graphs-for-the-knowledge-god](https://user-images.githubusercontent.com/5950433/222981558-0b50593a-c83f-4c6c-9aff-1b553403eac7.png)

- **What are the constraints:** We must consider our operational boundaries, threat models, trust in our inputs, alignment with strategic principles, and how to ensure our actions align with our goals. To manage these aspects, we can rely on AI but also use **SCITT** (Supply Chain Integrity, Transparency, and Trust) at each **Trusted Computing Base (TCB)** level.

- SCITT logs allow us to track and verify the flow of system contexts as they move through each level of the TCB. This ensures that all transitions are secure, fully transparent, and verifiable.
  - Each execution context will be appended to the **SCITT log**, which operates as an **append-only** ledger, ensuring an immutable history of state changes. This makes it possible to track how policies were applied and enforced at different stages.
  - By tying the **policy engine flows** to the **SCITT log**, we can verify that no unauthorized actions have occurred. Every decision made by the policy engine is logged and auditable.

- **AI as Individual Agents:** Imagine if each of us had our own versions of these truth-seeking AI agents—capable of navigating through complex system contexts, making secure decisions, and executing flows independently or cooperatively within a sandboxed environment. By distributing AI agents across various contexts, we can individually execute tasks in isolation or come together as a network of trusted agents to collaboratively solve more complex problems. Each AI, with access to a personalized SCITT log, can ensure that its actions remain secure and in alignment with the group’s goals.
  - This distributed approach would create a web of secure, verified processes that can not only scale but also adapt dynamically, leveraging the power of AI in a decentralized but coordinated fashion.
  
- **Federation for Context Sharing:** To truly harness the collective power of these AI agents, we must implement **federation**, where AIs share context across networks to coordinate their actions. Each AI agent within the federation can share and interpret context-dependent communication, forming **ad-hoc groups** to tackle specific challenges. These communications, often termed **side channels** in security, serve as specialized languages between agents, enabling them to discuss nuanced situations and potential threats based on shared context.
  
  - These side channels allow AIs to federate their operations and share insights about the environments they interact with, making context-aware decisions on the fly. This communication isn't static but evolves depending on the situation, allowing agents to form temporary alliances and execute coordinated flows to solve complex problems together. Side channels help AIs understand the subtle, context-dependent risks inherent in running shared dependencies on each other’s compute resources, enabling them to maintain a secure and resilient system.

## Executing a Flow Within a Sandbox

[![asciicast-2024-09-02: Rolling Alice: Architecting: Alice: A Shell for a Ghost: SSH LLM help from anywhere as long as you have a tmux session: install tpm2-tools on fedora](https://asciinema.org/a/674501.svg)](https://asciinema.org/a/674501?t=111)

Any unix machine (currently only fedora and debian-based distro dependencies are auto-installed. Passwordless sudo is recommended.) with tmux can set up an environment by running the following ssh command to get a "ghost" in your shell (inspired by https://localhost.run):

```bash
# From within TMUX
gh auth refresh -h github.com -s admin:public_key
for pub in $(find ~/.ssh -name \*.pub); do gh ssh-key add --title $(hostname)-$(basename $pub) $pub; done
export GITHUB_USER=$(gh auth status | grep 'Logged in to github.com account ' | awk '{print $7}')
ssh_alice() { ssh -p 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o PasswordAuthentication=no -R /tmp/${GITHUB_USER}.sock:$(echo $TMUX | sed -e 's/,.*//g') -R /tmp/${GITHUB_USER}-input.sock:/tmp/${GITHUB_USER}-input.sock ${GITHUB_USER}@alice.chadig.com; }
ssh_alice; sleep 1; ssh_alice
```

## Imagining AI Trust Networks

![such-alignment](https://user-images.githubusercontent.com/5950433/226707682-cfa8dbff-0908-4a34-8540-de729c62512f.png)

Imagine a world where AIs traverse an open network, independently searching for others to collaborate with and determine trustworthiness. These AIs, no longer confined to isolated environments, must cooperate, exchange information, and work together on shared tasks—such as developing software across a vast, shared dependency base.

As they encounter one another, the AIs must determine the trustworthiness of the flows they exchange. Each AI is responsible for reviewing flows submitted by others, which are designed to run on their compute environments. Before accepting any of these flows, the AIs must carefully evaluate the potential risks involved. Could this flow lead to a sandbox escape? Is the submitting AI aligned with the receiving AI’s risk tolerance?

To make these determinations, they don’t just need to understand sandbox security—they need to know how to escape the sandbox themselves. Mastery of this knowledge is crucial for accurately assessing the threat level of the code they receive. Every AI is simultaneously a gatekeeper and a participant, tasked with running computations but also safeguarding its own system from potential misuse.

These AIs are constantly balancing trust, risk, and collaboration. They negotiate access, run security checks through policy engines, and leverage **SCITT logs** at each **Trusted Computing Base (TCB)** level to verify that all actions are transparent and aligned with their own goals. By analyzing each other’s decision-making processes, they gain deeper insight into how to securely and efficiently develop software together, while ensuring that no AI is at risk of a security breach.

To facilitate their communication, the AIs use **federated context sharing**. As they form **ad-hoc groups** to work on joint tasks, they develop their own languages—known as **side channels** in security—unique to the context of their collaboration. These side channels enable the AIs to share subtle, real-time information about their environments, flows, and dependencies, ensuring that each agent understands the risks involved in sandbox escapes or software development on shared platforms.

This dynamic, evolving network of AIs continuously improves, learning not only how to work within the sandbox but also how to understand and assess the boundaries. It’s a system where mutual trust, context-sharing, and shared risk evaluations govern the open network—paving the way for a future of collaborative intelligence.

## /acc/

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
    - https://netflix.github.io/chaosmonkey/

![chaos-for-the-chaos-god](https://user-images.githubusercontent.com/5950433/220794351-4611804a-ac72-47aa-8954-cdb3c10d6a5b.jpg)

---

## Notes

- Flow
- Flow State
- Acceleration

### Flow

- What do we want to do?
  - Query
  - Response workflow

### Sandbox

- compute
- network
- switch_root on RoTs
- `uses`

### Links

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
