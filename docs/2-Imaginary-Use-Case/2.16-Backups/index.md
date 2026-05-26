# *"What if the server catches fire?"*

It sounds dramatic, but hardware fails. Hard drives die. Someone accidentally deletes a database. A botched update corrupts the system. One morning you arrive and the Proxmox host simply won't boot — the disk has bad sectors and half your containers are gone.

If you don't have backups, **everything you built is one bad day away from being gone**.

The golden standard is the **3-2-1 rule**: keep at least **3** copies of your data, on **2** different types of storage, with **1** copy off-site. For a community network running Proxmox, that means backing up every VM and container regularly, storing those backups on a separate disk or machine, and ideally replicating them to another building or a cloud endpoint.

**Proxmox Backup Server (PBS)** is built exactly for this. It is a dedicated backup system designed to work seamlessly with Proxmox VE. PBS supports **incremental backups** — after the first full backup, only the changes are transferred, saving time and disk space. It handles **deduplication** automatically, so identical blocks across different VMs are stored only once. And it integrates directly into the Proxmox web UI: you schedule backup jobs just like any other task, and restoring a VM or container to any previous point in time takes a few clicks.

You don't even need a dedicated machine for PBS. For small deployments, running it as a virtual machine or LXC container on a separate disk works well. What matters is that the backup storage is **physically separate** from the data it protects — a backup on the same disk as the original is not a backup at all.

!!! tip "Guide reference"
    For step-by-step PBS installation and configuration, see [Guide — Proxmox Backup Server](../../3-Guide/Proxmox-Backup-Server/index.md).
