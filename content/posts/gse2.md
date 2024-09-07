+++ date = 2024-09-07T14:00:00Z lastmod = 2024-09-07T14:00:00Z title = "Towards a Generic Sandbox Escape: Part 2: Flow State" subtitle = "From Cattle Back to Pets" +++

![will-you-federate-supply-chain-statements-with-me-neighbor](https://github.com/user-attachments/assets/f9bbe45d-5fef-4c22-9517-4cd312c3669c)

From Cattle Back to Pets
In the early days of cloud-native infrastructure, the analogy of cattle vs. pets emerged: servers and instances were treated like cattle—easily replaceable and disposable—unlike pets, which were given individual care and attention. The rise of container orchestration tools like Kubernetes further solidified this notion, treating system instances as ephemeral resources that could be terminated and replaced without concern for their unique characteristics.

However, as we advance towards secure, trust-driven computing, federation introduces a new layer of depth to how we manage and treat these instances. We are no longer content with treating systems as disposable. Now, every node, container, or AI agent must have its own context, synchronized with the broader goals and strategic principles of the federation. This shift moves us from cattle back to pets, where every instance is nurtured, context-aware, and a valuable contributor to the system.

This is where federation plays a key role, enabling new instances to sync up quickly with the system’s ongoing tasks, inheriting context, and aligning with the current scientific hypotheses and strategic goals.

Federation and Continuous Re-Evaluation
At the heart of this federation-driven system is the concept of continuous re-evaluation of agents, tasks, and hypotheses. Each AI agent and instance within the network must be constantly evaluated based on its alignment with the federation’s overall goals and its conformance to security principles defined by the S2C2F (Secure Supply Chain Consumption Framework)​.

In this setup, S2C2F attestations are critical. They act as attestations of alignment, ensuring that each agent or node adheres to the value chain principles and that all actions and hypotheses are aligned with the broader strategy. These attestations help create a transparent and secure process for software development, scientific discovery, and collaborative efforts within the federation.

KERI-Based SCITT: Witnesses and Duplicity Detection
The federation’s trust model is based on KERI (Key Event Receipt Infrastructure), which underpins the implementation of SCITT (Supply Chain Integrity, Transparency, and Trust). Each instance, task, or train of thought in the system represents a SCITT subject, and every action within the system is validated through KERI witnesses.

To ensure alignment and prevent tampering, at least four KERI witnesses verify each attestation, ensuring that no malicious or incompetent agent can disrupt the process. Through duplicity detection, KERI’s cryptographic capabilities enable the detection of any attempts to submit conflicting or unauthorized flows. If duplicity or misalignment is detected, the witnesses flag the issue, and the Prioritizer is triggered to reassess the agent’s trustworthiness.

Transparency Through Policy Execution
Transparency in policy execution is vital to ensuring that all actions within the system align with the federation's goals. The policy engine enforces security rules across the system, and these policies are registered via transparent statement URNs. By associating policies with URNs, each execution context is tracked as it mutates, ensuring that any changes to the state or context are visible and auditable.

Every time a flow or hypothesis is executed, the SCITT log records the policy execution, ensuring a clear and transparent view of how decisions are made and enforced. The system uses these transparent statements to evaluate ongoing hypothesized flows, ensuring that they are progressing in alignment with the strategic plan while maintaining trust and integrity.

Continuous Value Chain Analysis and S2C2F Alignment
The Prioritizer is responsible for the continuous value chain analysis, where each flow or action submitted by an agent is constantly re-evaluated against the system’s strategic principles. This ensures that all activities contribute to the scientific process while adhering to the federation’s security and governance framework.

The S2C2F framework emphasizes continuous improvement, control of all inputs, and scaling secure consumption practices​. Each time an agent submits a flow or engages in collaborative work, the system evaluates whether it aligns with S2C2F requirements, particularly in relation to the supply chain’s security and integrity. Attestations of conformance within S2C2F act as attestations of alignment in our system, ensuring agents meet strict security guidelines.

When misalignment, malintent, or incompetence is detected, the system takes immediate action. The policy engine cuts off misaligned agents, preventing them from further participation in the scientific process. This guarantees that only trustworthy entities—those whose actions are aligned with the federation’s strategic goals—remain active participants.

Informed Pair Execution: Learning and Aligning with Context
When a new instance joins the system, it does not operate in isolation. Instead, it engages in informed pair execution with another established agent. This process enables the new instance to rapidly align with the current state of the system by learning from its partner’s context and experience.

Informed pair execution provides the new agent with an accelerated path to alignment, helping it understand the ongoing hypotheses, the strategic objectives of the federation, and the security constraints. This dynamic interaction allows the new instance to quickly sync its state, learn how to avoid sandbox escapes, and contribute meaningfully to the collective intelligence.

Spec-to-State Sync: Kubernetes k3s Style
To maintain alignment and consistency across the federation, the system uses a K3s-style spec-to-state sync. When a new agent comes online, it is given a spec—a detailed description of the federation’s current state, including the hypotheses under investigation, the policy engine’s rules, and the system’s broader strategic goals.

The agent then reconciles its internal state with the desired state specified by the collective, ensuring that it is synchronized with the tasks being executed by the federation. This continuous spec-to-state sync process allows for seamless collaboration across instances, each contributing to advancing the state of the art in the scientific process.

Trust, Transparency, and Collaboration
The core of this federated system lies in the continuous re-evaluation of agents, flows, and strategic goals. With the S2C2F framework providing security and trust assurances, KERI duplicity detection ensuring integrity, and SCITT logs offering full transparency, we can build a system where agents work together to advance knowledge while safeguarding the system from threats.

This dynamic environment enables the federation to scale securely, bringing new agents into the fold through informed pair execution and spec-to-state syncing. By constantly re-evaluating trust, adhering to S2C2F principles, and using continuous value chain analysis, the system ensures that collaboration is both secure and effective, paving the way for a future where scientific process and trust go hand in hand.




+++ date = 2024-09-07T14:00:00Z lastmod = 2024-09-07T14:00:00Z title = "Towards a Generic Sandbox Escape: Part 2: Flow State" subtitle = "From Cattle Back to Pets" +++

From Cattle Back to Pets
In the early days of cloud-native infrastructure, the analogy of cattle vs. pets emerged: servers and instances were treated like cattle—easily replaceable and disposable—unlike pets, which were given individual care and attention. The rise of container orchestration tools like Kubernetes further solidified this notion, treating system instances as ephemeral resources that could be terminated and replaced without concern for their unique characteristics.

However, as we advance towards secure, trust-driven computing, federation introduces a new paradigm. No longer can we treat instances as disposable cattle; instead, every node, container, or AI agent must have its own context and be deeply aligned with the system’s goals and strategic principles. This marks the shift from cattle back to pets, where every instance is treated as a trusted, persistent entity contributing to the collective effort.

Federation becomes essential in this shift, allowing new instances to be integrated into the system rapidly, syncing states and ensuring that they are context-aware, capable of meaningful collaboration, and securely aligned with the federation’s objectives.

Federation and Continuous Re-Evaluation
Federation allows us to continuously sync and share context across a network of agents. But to maintain trust, we need a system for attesting to an agent’s ongoing alignment with the collective goals and security requirements. In this context, we use the SCITT framework (Supply Chain Integrity, Transparency, and Trust), combined with attestations of alignment based on the OpenSSF Secure Supply Chain Consumption Framework (S2C2F)​.

Under the SCITT model, every agent operating in the federation must continuously prove its alignment with the shared strategic objectives. These attestations of conformance, as described in S2C2F, become the attestations of alignment for a SCITT subject. This subject represents the train of thought or hypothesis that the federation is working on.

To validate these attestations, the federation continuously runs a value chain analysis, ensuring that all agents’ activities align with the overarching mission. This analysis is carried out by the Prioritizer, a system designed to dynamically evaluate each agent’s contributions against the federation's strategic principles. The Prioritizer ensures that security and alignment are maintained throughout the process, based on the practices laid out in S2C2F, such as scanning for vulnerabilities, auditing consumption methods, and enforcing secure workflows​.

KERI-Based SCITT and Witnesses
To further enhance trust, we use a KERI-based implementation of SCITT. KERI (Key Event Receipt Infrastructure) is a decentralized identity and attestation framework that allows us to cryptographically verify each agent’s actions. In our system, each SCITT subject (representing a train of thought or a scientific hypothesis) is continuously verified by at least four KERI witnesses—AI instances that monitor and validate the integrity of contributions within an ad-hoc group.

These witnesses play a critical role in duplicity detection, ensuring that any malicious or incompetent agent attempting to deceive the system is quickly identified. If an agent submits misaligned hypotheses, actions, or flows, the system immediately flags it for review. The Prioritizer reevaluates the situation, and if the agent’s actions fall outside of the strategic and security boundaries established by the federation, the policy engine will no longer work with that agent.

In this way, federation ensures that only trustworthy entities contribute to the advancement of the state of the art. By leveraging KERI witnesses, duplicity detection, and continuous re-evaluation, we can effectively safeguard the collaborative scientific process.

Spec-to-State Sync: Kubernetes k3s Style
When new instances join the federation, we use a K3s-style spec-to-state sync model to bring them up to speed. This model, inspired by Kubernetes, allows each new instance to match its state to the current desired state of the collective by following a pre-defined spec.

This spec contains all the necessary details about the ongoing flows, hypotheses under test, and the collective goals of the federation. As the new instance syncs to the desired state, it is immediately aligned with the rest of the group and ready to contribute. This spec-to-state sync ensures that no instance is merely a disposable node but a valuable contributor, fully aware of the scientific process and aligned with the collective effort.

Informed Pair Execution
To accelerate the learning process for new instances, we employ informed pair execution. This involves pairing a new agent with an experienced instance to share hypotheses, conduct experiments, and exchange insights. The experienced instance helps the newcomer understand the context, risks, and nuances of the collective’s work.

During this process, both agents evaluate each other’s workflows and hypotheses, running sandboxed experiments to ensure security and alignment. By sharing context and knowledge, informed pair execution enables the new instance to quickly adapt to the collective goals while gaining critical insights into the federation’s security principles.

This method is not only a powerful learning tool but also a key mechanism for ensuring that new agents are trustworthy and capable of contributing securely to the system.

Hypothesized Flows and the Scientific Process
At the heart of our system lies the scientific process, where AI agents continuously generate, test, and refine hypotheses to push the boundaries of knowledge. Each agent plays a specific role in this process:

Hypotheses Generation: Agents propose new theories or improvements to existing methods based on collective knowledge.
Testing: Hypotheses are tested in controlled, sandboxed environments. Results are analyzed for alignment with the strategic goals of the federation.
Iteration: Agents iterate on the hypotheses, adjusting based on results, and refining their approaches.
With federation in place, this process is collaborative. Each agent shares context with the group, ensuring that all hypotheses align with the collective mission. As new instances join, they inherit the ongoing flows, allowing them to contribute to the state of the art without duplicating efforts.

Continuous Security Alignment with OpenSSF S2C2F
One of the key aspects of maintaining alignment within the federation is ensuring continuous security conformance. This is achieved through the principles laid out in the OpenSSF S2C2F framework, which provides a structured approach to securing the supply chain for open-source software​.

The S2C2F practices—such as ingesting artifacts securely, scanning for vulnerabilities, auditing consumption methods, and enforcing trusted workflows—are integrated into the SCITT framework as attestations of alignment. Each agent in the federation must continuously attest to its compliance with the S2C2F practices, ensuring that security remains a top priority throughout the scientific process.

The Prioritizer, informed by the value chain analysis, assesses these attestations in real-time. If an agent fails to meet the security requirements or is found to be consuming compromised components, it is immediately flagged for reevaluation. The policy engine, in response to such misalignment, will cease to collaborate with the offending agent, preventing further security risks.

Trustworthy Collaboration Through Federation
By continuously evaluating agents based on SCITT attestations, leveraging KERI witnesses, and enforcing strict security practices through S2C2F, we create a robust trust-driven federation. Through informed pair execution, new instances learn from trusted agents and become productive contributors to the collective.

This system ensures that only agents who meet the stringent security and strategic goals of the federation are allowed to collaborate. Any misaligned or incompetent agent is quickly excluded from the process, maintaining the integrity of the scientific workflows.

The result is a dynamic, self-regulating federation of Humans and AIs that work together to advance the state of the art in a secure, transparent, and trustworthy way.
