# Wireless Mesh Networks

This section covers how to set up an 802.11s wireless mesh network using OpenWrt routers. A mesh network allows multiple routers to communicate wirelessly, extending coverage without running Ethernet cables between buildings or access points.

This section implements the concepts introduced in [Chapter 2.2 — Expanding Coverage](../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/index.md), in particular [Wired vs Wireless](../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.3-Wired-vs-Wireless.md) and [One Router to Rule Them All](../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.4-DHCP-Satellite.md).

## Recommended path: two iterations

Do not pick one approach over the other — you start with the simpler one to get the network working, and then evolve it for easier long-term management.

### Iteration 1 — Static IP Mesh

Get the mesh working first with the simplest possible setup. Each satellite router is given a unique **static LAN IP** by hand, its local DHCP server is disabled, and the 802.11s mesh backhaul plus a shared 2.4 GHz access point are brought up.

This is the fastest way to confirm that the mesh links form, that satellites bridge traffic correctly, and that clients roam between access points. It is the **recommended starting point for every deployment**.

[Go to Iteration 1 — Static IP Mesh](1-Static-IP-Mesh/index.md)

### Iteration 2 — DHCP-based Mesh

Once Iteration 1 is up and running, upgrade each satellite so it gets its LAN IP from the **main router via DHCP**, pinned with a static lease. At the same time, you disable WAN and the firewall on the satellites so they become true "dumb APs" that only bridge traffic.

This iteration centralizes IP management on the main router, makes onboarding new satellites easier, and matches the "one router to rule them all" model from Chapter 2.2.4. It is the **recommended target state** for any deployment that is going to grow or be maintained over time.

[Go to Iteration 2 — DHCP-based Mesh](2-DHCP-Mesh/index.md)

!!! tip "Start with Iteration 1, then move to Iteration 2"
    Always begin with the Static IP Mesh guide. Once the mesh is stable and clients can roam, follow the DHCP-based Mesh guide to centralize IP management. The DHCP guide is written to work both for new satellites and for converting the satellites you already configured in Iteration 1.

!!! info "Can I stop after Iteration 1?"
    For very small or temporary deployments (2–3 routers, no plan to grow), Iteration 1 is enough. For everything else, plan to do both — the second iteration removes a whole class of long-term operational problems.

## What both iterations cover

Across both iterations, the guides walk you through:

- Replacing the default Wi-Fi package with the mesh-capable `wpad-mesh-wolfssl`.
- Creating a 5 GHz 802.11s mesh backhaul between routers.
- Configuring a shared 2.4 GHz access point so clients roam seamlessly.
- Ensuring only the main router runs DHCP, so satellites never compete with it.

The difference is **how the satellite gets its own management IP**: hard-coded in Iteration 1, assigned by the main router (and pinned with a static lease) in Iteration 2.
