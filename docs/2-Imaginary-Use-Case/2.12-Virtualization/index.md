# *"One bad update took down Nextcloud, DNS, and Zabbix all at once!"*

Someone ran a system update on the mini PC that hosts all your services. The update changed a library that Nextcloud depended on, and Nextcloud broke. That would have been bad enough on its own, but Zabbix and the DNS server live on the same machine. The DNS process crashed during the update, and suddenly nobody in the network can resolve domain names. Zabbix is down too, so there are no alerts --- you find out because people start knocking on your door.

This is the fundamental problem with running everything on a single operating system. Services share libraries, compete for CPU and memory, and step on each other's files. When one thing goes wrong, everything goes wrong. In a community network where you are probably the only person who can fix things, that kind of cascading failure is devastating.

The solution is **virtualization** --- running each service in its own isolated environment on the same physical hardware. There are two main approaches. **Virtual machines** (VMs) emulate an entire computer with its own operating system kernel, which provides the strongest isolation but uses more resources. **Containers** share the host kernel but keep everything else separate --- files, processes, network interfaces --- so they are much lighter, often using only a few megabytes of RAM. For most community network services, containers are the better choice. You reserve full VMs for cases where you truly need a different operating system or complete hardware-level isolation.

**Proxmox VE** is the platform we use for this. It is free and open-source, runs on standard x86 hardware (a mini PC with an Intel N100 and 8 GB of RAM is enough to get started), and supports both LXC containers and KVM virtual machines through a web interface. You do not need to touch the command line for day-to-day operations. With Proxmox, that same mini PC can run a container for Nextcloud, another for Zabbix, another for DNS, and even a lightweight virtual OpenWrt router --- all isolated from each other. If Nextcloud crashes, your DNS keeps resolving. If you need to update Zabbix, you do it inside its container without risking anything else.

## Container or VM? A simple rule

You'll face this choice for every service you deploy, and a simple rule covers almost every case: **use a container unless you have a specific reason not to.** Containers (LXC, in Proxmox) are light, start in seconds, and let you pack many services onto modest hardware — exactly what a community network needs. Reach for a full **virtual machine** only when you genuinely need a *different operating system*, a custom kernel, or the strongest possible isolation between a workload and everything else. In practice that means most of your services — Nextcloud, DNS, Zabbix, a captive-portal backend — run happily in containers, and you keep VMs in reserve for the rare exception.

## Sizing the hardware

You don't need a server-room machine to start. A mini PC with an **Intel N100 and 8 GB of RAM** is enough to run a useful stack of containers, and it sips power — important where electricity is unreliable or off-grid. As a rough guide:

- **RAM is the first thing you run out of.** Most containers are happy with 256–512 MB; a database-backed service like Nextcloud wants 1–2 GB. Add up your services, then leave headroom — running at 90% memory is asking for trouble.
- **Storage matters more than CPU.** An N100 has plenty of compute for these workloads, but file-sharing and media services fill disks fast. Plan storage deliberately (the next section is entirely about this).
- **Leave room to grow.** Size for the services you'll add in six months, not just today's. When even a comfortable machine fills up, that's the signal to cluster — covered later in this chapter.

## Organizing your services

A little discipline here saves a lot of pain later. Give **each service its own container** rather than stacking several inside one — that's the whole point of the isolation. Name them clearly (`nextcloud`, `dns`, `zabbix`) so the Proxmox console reads like a map of your network. Keep a service's data on a predictable volume so backups are simple. And write down which container does what; the next volunteer — or you, in a year — will be grateful for it.

!!! tip "Guide reference"
    For step-by-step instructions, see the [Proxmox guides](../../3-Guide/Proxmox/index.md):

    - [Install Proxmox VE on Bare Metal](../../3-Guide/Proxmox/Install-Proxmox.md) --- download, install, and configure Proxmox on a dedicated machine.
    - [Run OpenWrt as an LXC Container](../../3-Guide/Proxmox/OpenWrt-LXC.md) --- deploy a virtual router inside Proxmox for routing and firewall duties.
