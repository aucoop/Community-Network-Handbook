# *"I've been configuring routers all week..."*

You now have twelve routers spread across three buildings. They're all running OpenWrt, they're all online, and for a while that felt like a triumph. Then reality set in. Last week you needed to change the WiFi password — a single, trivial change. You SSHed into the first router, edited the config, restarted the service. Then the second. Then the third. By the eighth you'd lost count of which ones you'd done. Somewhere in there you fat-fingered a setting on one of them, and you didn't find out until a teacher reported that her room's WiFi had a different password than everyone else's.

This is the wall every growing network hits. Configuration that's perfectly manageable on one or two devices becomes a part-time job on a dozen, and an impossible one on fifty. Every firmware update, every firewall tweak, every new SSID has to be repeated by hand on each device, and every repetition is another chance to make a mistake. Worse, the routers slowly **drift** apart — small inconsistencies creep in until no two are configured quite the same, and debugging becomes archaeology.

## One dashboard for the whole fleet

**OpenWISP** is an open-source network management platform built for exactly this problem. Instead of treating each router as a separate machine you log into, OpenWISP treats your routers as a **fleet** managed from a single dashboard. You define how a router should be configured — its WiFi networks, its firewall rules, its VPN settings — and OpenWISP pushes that configuration out and keeps the devices in sync. Think of it as a remote control for your entire network.

The shift this brings is bigger than convenience. A few of the things it changes:

- **Templates instead of repetition.** You write a configuration once as a template — "all access points have these two SSIDs, this firewall policy, this monitoring agent" — and apply it to every device in a group. Change the template, and the change propagates to every router that uses it. No more editing twelve files by hand.
- **Zero-touch provisioning.** A new router can register itself with OpenWISP when it first comes online and pull its configuration automatically. Mounting a replacement becomes a matter of powering it on, not an afternoon of SSH.
- **Consistency by default.** Because configuration flows from the central definition, drift stops happening. Every router that should be identical *is* identical, and you can prove it from the dashboard.
- **Monitoring and updates in one place.** OpenWISP also surfaces device status and can coordinate firmware upgrades across the fleet, so the same console that configures your network also tells you how it's doing.

## When it becomes worth it

OpenWISP is not free of cost — it's a server you have to run and learn. With two or three routers, doing things by hand is genuinely simpler, and you shouldn't bother. But there's a crossover point, usually somewhere around five to ten devices, where the time you spend repeating yourself (and fixing the mistakes that repetition causes) exceeds the time it takes to set up central management. Past that point, OpenWISP stops being overhead and becomes the only thing keeping the network sane.

!!! tip "Guide reference"
    For step-by-step OpenWISP setup, see [Guide — OpenWISP](../../3-Guide/OpenWISP/index.md).
