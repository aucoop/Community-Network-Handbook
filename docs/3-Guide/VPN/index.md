# VPN — Remote Access

Reach your network from anywhere in the world using encrypted WireGuard tunnels managed by Netmaker.

This section implements the concepts introduced in [Chapter 2 -- Remote Access](../../2-Imaginary-Use-Case/2.7-Remote-Access/index.md).

## Overview

A community network usually sits behind NAT, which means you cannot SSH into a router or access a web dashboard from outside unless you set up a VPN. The guides below use **Netmaker**, an open-source WireGuard orchestrator, to create a mesh VPN where every enrolled node can reach every other node directly through encrypted tunnels.

The setup has two parts:

1. **Server** -- A Netmaker instance running on a VPS with a public IP. It coordinates key exchange and configuration distribution but does not relay traffic.
2. **Clients** -- The Netclient agent installed on each OpenWrt router (and optionally on your laptop). It keeps WireGuard tunnels up and auto-updates when the network changes.

Once both parts are in place, you can manage the entire network remotely, route traffic between VPN nodes and local LANs via egress, and grant temporary access to volunteers through Netmaker's dashboard.

## Guides in This Section

- [Install Netmaker on a VPS](Netmaker-VPS.md) -- Deploy the Netmaker server that coordinates your WireGuard VPN network.
- [Install Netclient on OpenWrt](Netclient-OpenWrt.md) -- Enroll an OpenWrt router into the VPN and configure firewall zones, interface registration, and egress routing.

!!! info "Work in Progress"
    Future guides will cover manual WireGuard configuration (without Netmaker), split tunneling, and enrolling non-OpenWrt clients (laptops, phones, standard Linux servers).

<!-- TODO: Manual WireGuard guide, split tunneling, non-OpenWrt client enrollment -->
