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
