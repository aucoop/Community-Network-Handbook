# Wireless Mesh Networks

This section covers how to set up an 802.11s wireless mesh network using OpenWrt routers. A mesh network allows multiple routers to communicate wirelessly, extending coverage without running Ethernet cables between buildings or access points.

This section implements the concepts introduced in [Chapter 2.2 — Expanding Coverage](../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/index.md).

## Two Approaches

There are two common ways to configure satellite (secondary) routers in your mesh network. Both approaches create a working mesh, but they differ in how you manage IP addresses:

### 1. Static IP Mesh (Manual Assignment)

In this approach, you manually assign a unique static IP address to each satellite router before connecting it to the mesh. This is straightforward and works well for small deployments where you can easily track which IP belongs to which device.

**When to use:**

- Small networks with few satellites (2–5 routers)
- Quick initial testing and prototyping
- Situations where you want full control over IP assignments from the start

[Go to Static IP Mesh Guide](1-Static-IP-Mesh/index.md)

### 2. DHCP-Based Mesh (Automatic Assignment)

In this approach, satellites request their IP address from the main router via DHCP, just like any other client device. You then create a static DHCP lease on the main router to ensure the satellite always receives the same IP.

**When to use:**

- Larger networks with many satellites
- When you want centralized IP management from the main router
- When adding new satellites frequently (easier onboarding)

[Go to DHCP-Based Mesh Guide](2-DHCP-Mesh/index.md)

## Which Should You Choose?

| Factor | Static IP | DHCP-Based |
|--------|-----------|------------|
| Setup complexity | Simpler initial config | Slightly more steps |
| IP management | Distributed (on each device) | Centralized (main router) |
| Adding new satellites | Manual IP planning | Automatic, then pin with lease |
| Troubleshooting | IP always known | Must check DHCP leases |
| Best for | Small, stable networks | Growing, dynamic networks |

!!! tip "Start with Static; migrate to DHCP later"
    If you're new to mesh networking, start with the **Static IP Mesh** guide to get your network running quickly. Once you're comfortable, you can migrate satellites to the **DHCP-Based** approach for easier long-term management — the [DHCP guide](2-DHCP-Mesh/index.md) explains how to convert existing satellites.

## Common to Both Approaches

Regardless of which IP assignment method you choose, both guides cover:

- Replacing the default Wi-Fi package with the mesh-capable `wpad-mesh-wolfssl`
- Creating a 5 GHz 802.11s mesh backhaul between routers
- Configuring a shared 2.4 GHz access point for end users
- Disabling DHCP server on satellites to avoid conflicts
