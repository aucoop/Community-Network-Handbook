# *"The power went out and everything died"*

It happens at 2 AM. A power surge, or just a regular outage — common in many parts of the world. Your server reboots ungracefully. A hard drive gets corrupted. The Proxmox host comes back but two containers don't start.

In places where power is unreliable, you need:

- **UPS (Uninterruptible Power Supply)** — a battery that gives your servers time to shut down gracefully during an outage
- **Surge protectors** — protect equipment from voltage spikes
- **Solar panels** — in off-grid or unreliable-grid locations, solar can be a primary or backup power source
- **Graceful shutdown scripts** — configure Proxmox to shut down cleanly when the UPS battery runs low

!!! info "Work in Progress"
    This section will cover power planning for community networks in areas with unreliable electricity.

!!! tip "Guide reference"
    For UPS and power setup, see [Guide — Power and UPS](../../3-Guide/Power-and-UPS/index.md).

<!-- TODO: UPS sizing, NUT (Network UPS Tools), solar basics, power budget calculation -->
