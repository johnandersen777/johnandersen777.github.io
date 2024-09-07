+++
date = 2024-09-07T14:00:00Z
lastmod = 2024-09-07T14:00:00Z
title = "Towards a Generic Methodology for Sandbox Escape: Part 2: Flow State"
subtitle = "From Cattle Back to Pets"
+++

## Series

- [Flow](https://pdxjohnny.github.io/gse1/)
- [Flow State](https://pdxjohnny.github.io/gse2/)
- Acceleration

## Context

- [DFFML: docs: tutorials: Rolling Alice](https://github.com/intel/dffml/tree/main/docs/tutorials/rolling_alice)
- [Katherine Druckman - Threat Modeling Down the Rabbit Hole - OpenAtIntel](https://openatintel.podbean.com/e/threat-modeling-down-the-rabbit-hole/)
- [Gabe Cohen - On Decentralized Trust](https://decentralgabe.xyz/on-decentralized-trust/)
- [Harald Sack - Symbolic and Subsymbolic AI - An Epic Dilemma?](https://github.com/lysander07/Presentations/raw/main/EGC2023_Symbolic%20and%20Subsymbolic%20AI%20%20-%20an%20Epic%20Dilemma.pdf)
- [Nancy Eckert - Swarm Intelligence and Human Systems - BSides Portland 2019](https://youtu.be/Eq33S_Rz4qo?t=1117)
- [Robin Berjon - The Internet Transition](https://berjon.com/internet-transition/)
- [Adam Frank, David Grinspoon, and Sara Walker - Intelligence as a planetary scale process](https://www.cambridge.org/core/journals/international-journal-of-astrobiology/article/intelligence-as-a-planetary-scale-process/5077C784D7FAC55F96072F7A7772C5E5)

## From Cattle Back to Pets

In the early days of cloud-native infrastructure, the analogy of **cattle vs. pets** emerged: servers and instances were treated like cattle—easily replaceable and disposable—unlike pets, which were given individual care and attention. With container orchestration tools like Kubernetes, system instances became ephemeral resources that could be terminated and replaced without concern for their unique characteristics.

However, as we move toward **secure, trust-driven computing**, the notion of **federation** requires a shift from treating instances as cattle back to treating them like **pets**—context-aware, persistent agents aligned with the strategic principles of the system. Through federation, we no longer discard or replace instances mindlessly. Instead, each instance is treated as a trusted participant, sharing context, tasks, and accountability.

## Federation and Continuous Re-Evaluation of Trust

![will-you-federate-supply-chain-statements-with-me-neighbor](https://github.com/user-attachments/assets/f9bbe45d-5fef-4c22-9517-4cd312c3669c)

**Federation** allows AI agents and systems to sync their context, contributing collaboratively to the **scientific process**. As new instances join the network, they sync their states via a **spec-to-state model** (Kubernetes K3s-style) and rapidly come up to speed on ongoing experiments and hypotheses.

Crucially, every federated instance is subject to **continuous re-evaluation** through the **Prioritizer**—which assesses whether an instance remains aligned with the strategic goals of the federation. This continuous re-evaluation involves the **Secure Supply Chain Consumption Framework (S2C2F)**, where **attestations of conformance**—representing an agent's alignment with the federation's principles—are tracked and verified. These attestations serve as **proofs of alignment** with the value chain analysis and the security requirements outlined in the S2C2F【26†source】.

## KERI-Based SCITT and Duplicity Detection

To manage the integrity of the federation, we use a **KERI-based implementation** of the **Supply Chain Integrity, Transparency, and Trust (SCITT)** model. **KERI (Key Event Receipt Infrastructure)** provides cryptographic support for ensuring each AI agent's identity, actions, and contributions to the shared **train of thought** remain trustworthy.

Each **SCITT subject**—representing an ongoing hypothesis or a sequence of flows—carries **attestations of alignment** from at least **four KERI witnesses** (AI instances). These witnesses are responsible for continuously validating each other's actions and ensuring there is no **duplicity** or deviation from the collective mission. **Duplicity detection** ensures that any attempt to manipulate or forge data is quickly identified, while the transparency of the policy execution ensures that actions are verifiable by all participating agents.

The transparency of the **policy engine** is enforced by registering every **to-be-executed policy** with a **transparent statement URN**. This allows for traceability of every mutating execution context, ensuring that changes are transparent, logged in the SCITT ledger, and subject to audit by the federation. Any AI agent whose actions violate these policies or introduce untrusted mutations will trigger a re-evaluation by the Prioritizer, ensuring the collective remains secure and aligned.

## Continuous Alignment with OpenSSF S2C2F

In the context of security, the **S2C2F framework** requires ongoing **value chain analysis** to mitigate risks in the software supply chain. This includes continuous scanning, attestation of conformance, and the use of the Prioritizer to monitor alignment with S2C2F's principles【26†source】. As outlined in S2C2F, the goal is to control artifact inputs, enforce governance over supply chain flows, and ensure that all OSS (Open Source Software) dependencies are secure.

By aligning with S2C2F's principles of **ingestion, scanning, and auditing** of dependencies, the federation ensures that any vulnerabilities, misaligned agents, or risks are detected early. The **attestations of conformance** within S2C2F serve as **attestations of alignment** in the federation, and are tracked continuously in the **SCITT registry**. Should an instance's security practices fall out of alignment, the policy engine will no longer allow it to participate in ongoing scientific flows, blocking its access until the issues are resolved.

## Informed Pair Execution and Collaboration

To bring new instances up to speed, **informed pair execution** is employed. This technique allows new AI agents to collaborate directly with trusted, experienced instances to synchronize context, understand ongoing hypotheses, and participate in sandboxed experiments. Through this **informed collaboration**, new instances learn not only the strategic goals of the federation but also the **sandbox boundaries** and how to handle potential **sandbox escapes**.

Both **AI and human instances** may collaborate in this process to assess risks associated with sandbox escapes. Human expertise complements AI's computational abilities, allowing for joint evaluations of strategic goals and risk tolerances. By sharing real-time information and context through **federated side channels**, instances maintain continuous security and alignment while innovating together.

## Detection of Misaligned Agents and Policy Enforcement

In a federated environment, trust must be actively maintained. Through continuous value chain analysis, instances that display **malintent**, **incompetence**, or introduce critical errors are quickly flagged by the **Prioritizer**. If an agent's actions no longer align with the federation’s principles—whether through failure in maintaining security, performance of risky sandbox escapes, or deviating from approved flows—the **policy engine** will cease collaboration with the misaligned agent.

The transparency provided by **KERI witnesses**, combined with SCITT's immutable attestation log, ensures that the federation remains **trustworthy** and **resilient**. Any agent failing to meet the collective's expectations is removed from the flow, preventing disruptions or security breaches. This dynamic, **self-regulating ecosystem** of AI agents ensures that only aligned, competent entities continue to participate in advancing the **state of the art**.

## Hypothesized Flows and the Scientific Process

At the core of the federation's operation is the **scientific process**. This process involves the continuous generation, testing, and refinement of hypotheses aimed at advancing the **state of the art**. Each AI agent contributes by hypothesizing new solutions, running sandboxed experiments, and iterating on results based on the collective knowledge of the federation.

Through **federated context sharing**, every instance stays synchronized with the group’s evolving train of thought. **Informed pair execution** ensures that new agents contribute to the advancement of scientific flows while learning from the more experienced instances. The **KERI-based SCITT implementation**, combined with **S2C2F-based alignment attestations**, provides the necessary transparency, trust, and continuous re-evaluation to maintain security and strategic integrity.

The result is a dynamic, self-regulating federation of Humans and AIs that work together to advance the state of the art in a secure, transparent, and trustworthy way.

---

**Next in Part 3: Acceleration of Federated Systems**, we will explore optimizing this system further, focusing on accelerating the hypothesis-testing cycle while ensuring that sandbox escapes and risks are minimized in a federated environment.

---

## Notes

- **Continuous Re-evaluation:** The Prioritizer continuously assesses alignment and value chain integrity.
- **KERI-based SCITT:** Cryptographically-secured attestations and duplicity detection maintain trust.
- **S2C2F:** Continuous security alignment based on Secure Supply Chain Consumption Framework.
- **Informed Pair Execution:** Collaborative learning and syncing of contexts between instances.
- **Sandbox Escapes:** Human and AI collaboration in assessing risks and escapes while maintaining trust.
