+++
date = 2024-09-06T14:00:00Z
lastmod = 2024-09-06T14:00:00Z
title = "Towards a Generic Sandbox Escape: Part 1: Flow"
subtitle = "First enable flow. Next enter flow state"
+++

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
