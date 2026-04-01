# VPN — Remote Access

Reach your network from anywhere in the world using encrypted WireGuard tunnels managed by Netmaker.

This section implements the concepts introduced in [Chapter 2 -- Remote Access](../../2-Imaginary-Use-Case/2.7-Remote-Access/index.md).

## Overview

A community network usually sits behind NAT, which means you cannot SSH into a router or access a web dashboard from outside unless you set up a VPN. The guides below use **Netmaker**, an open-source WireGuard orchestrator, to create a mesh VPN where every enrolled node can reach every other node directly through encrypted tunnels.

The setup has two parts:

1. [**Server**](Netmaker-VPS.md) -- A Netmaker instance running on a VPS with a public IP. It coordinates key exchange and configuration distribution but does not relay traffic.
2. **Clients** -- Devices that join the network. There are two methods:
    - [**Netclient agent**](Netclient-OpenWrt.md) -- installed on OpenWrt routers and Linux servers. It auto-updates tunnels when the network changes.
    - [**WireGuard config file**](WireGuard-Config.md) -- generated from the Netmaker dashboard and imported on any device (laptop, phone, server). Simpler, but static -- you re-download the config if the network changes.

Once both parts are in place, you can manage the entire network remotely, route traffic between VPN nodes and local LANs via egress, and grant temporary access to volunteers through Netmaker's dashboard.

## Guides in This Section

- [Install Netmaker on a VPS](Netmaker-VPS.md) -- Deploy the Netmaker server that coordinates your WireGuard VPN network.
- [Install Netclient on OpenWrt](Netclient-OpenWrt.md) -- Enroll an OpenWrt router into the VPN and configure firewall zones, interface registration, and egress routing.
- [Add a Device via WireGuard Config File](WireGuard-Config.md) -- Connect any device (laptop, phone, server) using a config file generated from the Netmaker dashboard.

