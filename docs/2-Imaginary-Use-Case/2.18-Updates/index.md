# *"When was the last time we updated anything?"*

Everything is running smoothly. So smoothly, in fact, that you haven't logged into anything in six months — there was never a reason to. Then you finally do, and the picture is uncomfortable. The OpenWrt firmware is three releases behind. Proxmox is flagging security updates you've never applied. Nextcloud has been nagging for weeks about an unsupported PHP version. Nothing is *broken* — which is exactly why nobody touched it — but the whole stack has quietly aged, and every month of neglect makes the eventual catch-up riskier.

This is the paradox of maintenance: a healthy network gives you no reason to maintain it, right up until the day an unpatched vulnerability or a creeping incompatibility takes it down. **Maintenance isn't glamorous, and it's invisible when it's working — but it's the difference between a network that lasts years and one that decays into an emergency.**

## What neglect actually costs

Skipping updates doesn't keep things stable; it trades small, scheduled effort now for large, unscheduled effort later. Specifically, it lets four problems accumulate:

- **Security vulnerabilities** — unpatched software is the single most common way networks get compromised. Most fixes that matter are security fixes, and the longer you wait, the more known holes sit open.
- **Compatibility drift** — old server versions slowly stop working with new client devices and new versions of the software around them. What worked with last year's phones may not work with this year's.
- **Performance and reliability bugs** — updates carry bug fixes and optimizations, not just features. Running old means living with problems that were solved months ago.
- **Knowledge loss** — the quietest failure. If nobody writes down what's running and why, the person who inherits the network can't maintain it at all. Undocumented infrastructure has an expiry date: the day its builder walks away.

## Make it a routine, not a rescue

The goal is to turn maintenance from a dreaded, risky catch-up into a small, boring habit. A few practices make that possible:

- **A regular schedule.** Pick a cadence — say, security patches monthly and a fuller review each quarter — and put it on a calendar. Little and often beats heroic and rare, and small updates are far less likely to break things than six months applied at once.
- **Back up before you update.** This is the rule that makes updates safe to attempt. With the backups from earlier in this chapter, an update that goes wrong is a quick restore, not a disaster — which means you can actually keep up to date without fear.
- **Update one thing at a time and watch it.** Patch a service, confirm it still works, then move on. If something breaks, you know exactly what caused it — and your monitoring (Zabbix) will tell you fast if it does.
- **Keep a simple change log.** Write down what you changed and when — a shared document is plenty. It makes troubleshooting trivial ("what changed before this broke?") and it's the core of the knowledge that lets the network outlive any one volunteer.

Maintenance is where everything else in this chapter — backups, monitoring, security, documentation — comes together into the simple discipline that keeps the whole network alive.

!!! tip "Guide reference"
    For a maintenance checklist and update routines, see [Guide — Updates and Maintenance](../../3-Guide/Updates-and-Maintenance/index.md).
