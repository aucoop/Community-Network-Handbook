# Glossary

A quick reference for acronyms and terms used throughout this handbook. Most entries link to the Guide topic where the term is used in depth.

## A

- **AP — Access Point.** A device that provides Wi-Fi to client devices. Often the same physical hardware as a router, with one or more radios configured as APs.
- **AUCOOP.** Associació d'Universitaris per a la Cooperació — a student volunteer association at the Universitat Politècnica de Catalunya (UPC) in Barcelona. Maintains this handbook.

## B

- **Backhaul.** The link that carries traffic from a local access point back to the rest of the network. Often a wireless point-to-point link in community deployments.
- **BSSID.** The MAC address of a Wi-Fi access point's radio. Lets clients distinguish between APs even when they share the same SSID.

## C

- **Captive portal.** A welcome page shown the first time a user connects to a Wi-Fi network — often used for terms of use or guest authentication. See [Captive Portal](3-Guide/Captive-Portal/index.md).
- **CIDR.** Classless Inter-Domain Routing — the `/24`-style notation for IP subnets. See [IP Addressing](3-Guide/IP-Addressing/index.md).
- **CPE — Customer Premises Equipment.** A device installed at the user end of a link — typically an outdoor antenna mounted on a building.

## D

- **DHCP.** Dynamic Host Configuration Protocol — automatically hands out IP addresses to devices that connect to the network.
- **DNS.** Domain Name System — turns names like `nextcloud.example.org` into IP addresses. See [DNS](3-Guide/DNS/index.md).

## F

- **FOSS — Free and Open Source Software.** Software that is free to use, study, modify, and redistribute. This handbook commits to a FOSS-first stack.

## G

- **Gateway.** The device that routes traffic out of the local network towards the wider internet (or towards another network).

## I

- **IP address.** The numeric address of a device on a network. See [IP Addressing](3-Guide/IP-Addressing/index.md).

## L

- **LXC — Linux Containers.** A lightweight virtualisation technology used by Proxmox. See [Proxmox](3-Guide/Proxmox/index.md).

## M

- **Mesh.** A network topology where every node can relay traffic for other nodes, instead of all traffic going through a central point. See [Wireless Mesh](3-Guide/Wireless-Mesh/index.md).
- **MTU — Maximum Transmission Unit.** The largest packet size a network link can carry without fragmentation.

## N

- **NAS — Network Attached Storage.** A dedicated device that provides shared file storage to the network. See [Storage](3-Guide/Storage/index.md).
- **NAT — Network Address Translation.** Lets many devices share a single public IP address.
- **Netmaker.** A management overlay built on WireGuard. See [VPN](3-Guide/VPN/index.md).

## O

- **OpenWISP.** A platform for centrally managing fleets of OpenWrt devices. See [OpenWISP](3-Guide/OpenWISP/index.md).
- **OpenWrt.** An open-source Linux-based firmware for routers and access points. See [Flash OpenWrt](3-Guide/Flash-OpenWrt/index.md).

## P

- **PoE — Power over Ethernet.** Carries electrical power and data over the same Ethernet cable. Common for outdoor APs and antennas.
- **Proxmox VE.** An open-source type-1 hypervisor that runs VMs and LXC containers on a single server. See [Proxmox](3-Guide/Proxmox/index.md).

## R

- **RADIUS.** A protocol for centralised user authentication. See [RADIUS](3-Guide/RADIUS/index.md).

## S

- **SNMP — Simple Network Management Protocol.** Used by monitoring tools to collect metrics from network devices.
- **SSH — Secure Shell.** An encrypted protocol for remote command-line access to a device. The standard way to administer routers, servers, and APs over the network.
- **SSID.** The human-readable name of a Wi-Fi network.
- **Subnet.** A subdivision of an IP network. Each subnet has its own address range.

## U

- **UCI — Unified Configuration Interface.** OpenWrt's configuration system. One consistent format for every part of the firmware.
- **UPS — Uninterruptible Power Supply.** A battery that keeps equipment running through short power cuts. See [Power and UPS](3-Guide/Power-and-UPS/index.md).

## V

- **VLAN — Virtual LAN.** A way to split one physical network into multiple logical ones.
- **VM — Virtual Machine.** A full guest operating system running on a hypervisor.
- **VPN — Virtual Private Network.** An encrypted tunnel between machines or networks. See [VPN](3-Guide/VPN/index.md).

## W

- **WireGuard.** A modern, lightweight VPN protocol built into the Linux kernel. See [VPN](3-Guide/VPN/index.md).
- **WPA2 / WPA3.** Wi-Fi encryption standards. WPA3 is newer; WPA2 is still widely supported.

## Z

- **Zabbix.** An open-source infrastructure monitoring system. See [Zabbix](3-Guide/Zabbix/index.md).
