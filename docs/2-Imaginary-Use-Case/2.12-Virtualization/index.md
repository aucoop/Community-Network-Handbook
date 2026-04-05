# *"One bad update took down Nextcloud, DNS, and Zabbix all at once!"*

Someone ran a system update on the mini PC that hosts all your services. The update changed a library that Nextcloud depended on, and Nextcloud broke. That would have been bad enough on its own, but Zabbix and the DNS server live on the same machine. The DNS process crashed during the update, and suddenly nobody in the network can resolve domain names. Zabbix is down too, so there are no alerts --- you find out because people start knocking on your door.

This is the fundamental problem with running everything on a single operating system. Services share libraries, compete for CPU and memory, and step on each other's files. When one thing goes wrong, everything goes wrong. In a community network where you are probably the only person who can fix things, that kind of cascading failure is devastating.

The solution is **virtualization** --- running each service in its own isolated environment on the same physical hardware. There are two main approaches. **Virtual machines** (VMs) emulate an entire computer with its own operating system kernel, which provides the strongest isolation but uses more resources. **Containers** share the host kernel but keep everything else separate --- files, processes, network interfaces --- so they are much lighter, often using only a few megabytes of RAM. For most community network services, containers are the better choice. You reserve full VMs for cases where you truly need a different operating system or complete hardware-level isolation.

**Proxmox VE** is the platform we use for this. It is free and open-source, runs on standard x86 hardware (a mini PC with an Intel N100 and 8 GB of RAM is enough to get started), and supports both LXC containers and KVM virtual machines through a web interface. You do not need to touch the command line for day-to-day operations. With Proxmox, that same mini PC can run a container for Nextcloud, another for Zabbix, another for DNS, and even a lightweight virtual OpenWrt router --- all isolated from each other. If Nextcloud crashes, your DNS keeps resolving. If you need to update Zabbix, you do it inside its container without risking anything else.

!!! info "Work in Progress"
    This section will be expanded with more detail on container vs VM trade-offs, minimum hardware sizing for different workloads, and strategies for organizing services across containers.

!!! tip "Guide reference"
    For step-by-step instructions, see the [Proxmox guides](../../3-Guide/Proxmox/index.md):

    - [Install Proxmox VE on Bare Metal](../../3-Guide/Proxmox/Install-Proxmox.md) --- download, install, and configure Proxmox on a dedicated machine.
    - [Run OpenWrt as an LXC Container](../../3-Guide/Proxmox/OpenWrt-LXC.md) --- deploy a virtual router inside Proxmox for routing and firewall duties.

<!-- TODO: Container vs VM decision framework, hardware sizing table, service organization strategies -->
