# *"The power went out and everything died"*

It happens at 2 AM. The grid drops — a surge, a substation fault, or just one of the routine outages that are part of daily life in much of the world. Your equipment doesn't shut down gracefully; it simply *stops*, mid-write, in the dark. When the power comes back an hour later, the Proxmox host reboots, but two containers won't start. A filesystem check finds corruption. One disk now reports errors it didn't have yesterday. The outage lasted an hour; the damage lasts a week.

This is one of the most underestimated threats to a community network, precisely because it has nothing to do with networking. You can design a perfect topology and harden every service, and an unstable power supply will still quietly destroy your hardware and your data. In places where the grid is unreliable, **power is not a detail — it's part of the infrastructure**, and it has to be planned as deliberately as the network itself.

## The two ways power hurts you

Bad power does damage in two distinct ways, and you need to defend against both:

- **Sudden loss of power** cuts off a machine mid-operation. Disks writing at that instant can corrupt, databases can be left inconsistent, and filesystems can need repair. The fix is to give the machine *time* — enough to finish what it's doing and shut down cleanly.
- **Dirty power** — surges, spikes, brownouts, and sags — physically stresses the electronics. Over months it degrades components and shortens hardware life; a single big surge can kill a device outright. The fix is to put something between the grid and your equipment that absorbs the abuse.

## Building a resilient power chain

A practical setup layers a few inexpensive pieces:

- **UPS (Uninterruptible Power Supply)** — the cornerstone. A UPS is a battery that sits between the wall and your equipment. When the grid drops, it carries the load for a few minutes — not to keep the network running through a long outage, but to give your servers time to shut down *cleanly* instead of crashing. This single device prevents most outage-related corruption.
- **Surge protection** — guards against voltage spikes. Many UPS units include surge protection; in areas with especially dirty power, a dedicated voltage regulator or stabilizer is worth adding.
- **Graceful shutdown automation** — the piece people forget. A UPS only helps if your servers *know* the power is out and act on it. Tools like **NUT (Network UPS Tools)** let the UPS signal Proxmox over USB or the network: when the battery runs low, NUT triggers a clean, automatic shutdown of the host and its VMs. Without it, the UPS just delays the crash instead of preventing it.
- **Solar** — in off-grid or chronically unreliable locations, solar panels with a battery bank can serve as a primary or backup power source. Community networks have run for years on modest solar setups; it's a larger project, but it can turn "the power is a problem" into "the power is solved."

## Size it to what you're protecting

You don't need to power the whole building — just the equipment that must survive an outage cleanly: the router(s), the switch, and the server. Add up their wattage, decide how many minutes of runtime you want (enough to ride out brief blips and to shut down safely on longer ones), and size the UPS to match. A modest UPS protecting the core gear is far more valuable than an oversized one you never quite got around to buying.

!!! tip "Guide reference"
    For UPS sizing, NUT configuration, and power planning, see [Guide — Power and UPS](../../3-Guide/Power-and-UPS/index.md).
