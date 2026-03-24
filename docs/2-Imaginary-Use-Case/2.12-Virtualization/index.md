# *"I can't keep running everything on this tiny router!"*

You've been installing services directly on a mini PC or even on one of the routers. It worked for Nextcloud, but now you want to add Zabbix, a DNS server, a VPN server, and a RADIUS server. They're all fighting over resources and conflicting with each other.

You need **virtualization** — the ability to run multiple isolated "virtual machines" or "containers" on a single physical server. **Proxmox VE** is a free, open-source platform that does exactly this.

With Proxmox, one physical machine can run:

- A container for Nextcloud
- A container for Zabbix
- A container for DNS
- A virtual machine for anything that needs full isolation

Each one is independent. If Nextcloud crashes, your DNS server keeps running.

!!! info "Work in Progress"
    This section will introduce virtualization concepts and explain why Proxmox is a good fit for community networks.

!!! tip "Guide reference"
    For step-by-step Proxmox setup, see [Guide — Proxmox](../../3-Guide/Proxmox/index.md).

<!-- TODO: Containers vs VMs, Proxmox overview, minimum hardware requirements -->
