+++
date = 2026-04-30T21:50:00Z
lastmod = 2026-04-30T21:50:00Z
title = "Sandbox"
subtitle = "Sandbox for CI/CD and AI"
+++

- want to use vhost ssh unix socket forwarding to expose creds via wid rproxy to guess as unix perm file

- could maybe just tun MITM all trafic and replace certs in guest

- why not just offer a sandboxed runtime?

  - deno or python or wasm
 
  - Then package management would be standard
 
  - Expose clean interfaces between runner and orchestrator
 
  - Keep it standard lang -> no jenkins groovy
 
- atproto (obvi)

- spiffie wid rproxy

- tpm host -> tpm guest -> verifier -> SCITT

  - SPIFFIE endpoint expose attestation / verifier siger for scitt or something? 

  - "free" decentralized pool

  - attested & reproducable builds tracks
 
---

- https://openid.net/specs/openid-federation-1_0.html

- atrprp.chadig.com

  - service.handle.com.atrprp.chadig.com
 
- sh.tagled.publicKey

- emit firehose event if we need a reconnect (example: scalling to more nodes)

- ssh -R or -L (which one is it again?)

- if web of trust via vouches says you're good then enable for user

- https://github.com/publicdomainrelay/sshai/blob/b309c3d64498985b132f61543dde1929cbcdb687/src/sshd/agi_sshd.go#L81

  - ssh reverse proxy

- could support only certain software via attestations or workload id and trust rings

- User adds record for service

  - User (or service via workload id) adds ssh key

  - backlinks ssh keys to service
 
- proxy gets request over ssh

  - splits service.handle.com
 
  - resolves service records
 
  - checks ssh keys valid using backlinks to keys
 
  - ensures caddy reverse proxies to unix socket (maybe future support for round robin if multiple active connections)

- User goes to atprp.chadig.com

  - adds service name and ssh keys for backend(s)
 
  - PoC round 1 use https://pdsls.dev to create records

    - https://pdsls.dev/at://did:plc:5svqtrhheairglgiiyvutzik/sh.tangled.publicKey/3mgwzjaw6vu22
   
    - https://constellation.microcosm.blue/xrpc/blue.microcosm.links.getBacklinks?subject=at%3A%2F%2Fdid%3Aplc%3Aa4pqq234yw7fqbddawjo7y35%2Fapp.bsky.feed.post%2F3m237ilwc372e&source=app.bsky.feed.like%3Asubject.uri&limit=16

- on system we want to reverse proxy to

  - uv run or curl to bash for install
 
  - `UserKnownHostsFile` download public key over HTTPS 

  - install systemd unit files to restart ssh proxy to local port on restart
   
    - https://github.com/johnandersen777/dotfiles/blob/8726281467c5ababe53fc1e2d869a8e897c89cf8/forge-install.sh#L59-L74

---

> https://bsky.app/profile/filippo.abyssdomain.expert/post/3mkldvg6iec2h
>
> Alright, wishlist for a GitHub replacement.
>
> Obvious:
>
> - actually read-only CI jobs
> - CI configs safer than interpolated shell in YAML
> - git pushes don’t just shell out under user git (!!)
> - uptime??
>
> Less obvious:
>
> - git pushes tlog
> - unprivileged agent sub-accounts
> - decent vuln scanner

---

> https://pnsqc.org
> 
> Tools & Productivity
>
> For practitioners and tool builders demonstrating how work actually gets done, with concrete workflows and lessons learned. Papers will show conditions before vs after, and will mention what doesn't work.
>
> This track focuses on practical tools, frameworks, and techniques that improve the productivity and effectiveness of quality engineering teams. Submissions should emphasize real-world experience, engineering insights, and lessons learned from building, integrating, or applying tools in modern software development environments.
>
> Submissions should focus on technical insights and practical experience rather than product demonstrations or sales presentations.
> Tools may be referenced, but talks should provide lessons and techniques that other teams can apply.
>
> Topics May Include
> - Test automation platforms and frameworks
> - Developer productivity and testing workflows
> - Observability, diagnostics, and debugging tools
> - CI/CD testing infrastructure
> - Managing flaky tests and test reliability
> - AI-assisted testing tools and practices
> - Toolchains for modern quality engineering
> - Integrating testing into developer workflows
> - Scaling test automation in large systems
>
> Example Paper Titles
> - Lessons Learned Building AI-Generated Test Suites
> - Managing Flaky Tests in CI at Scale
> - Using Observability Data to Diagnose Test Failures
> - Integrating Quality Signals into Developer Workflows
> - Tooling Strategies for Testing Microservices
> - Improving Test Feedback Loops for Developers
> - Reducing Test Execution Time in Large CI Pipelines
> - Making Test Automation Maintainable Over Time

