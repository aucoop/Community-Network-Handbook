# *"Wait... is any of this actually secure?"*

You've been so focused on making things *work* that you never stopped to ask whether any of it is safe. The realization tends to arrive all at once, usually late at night: the WiFi password is a single shared phrase that, by now, half the town knows. You've been opening firewall ports one at a time as you added services, and you're no longer sure which ones are still open or why. The firmware on some routers hasn't been touched since the day you flashed it. SSH on the main server still accepts password logins. If someone wanted in, you've left several doors unlocked — you just haven't noticed because nobody's tried the handles yet.

Here's the reframing that helps: you don't need enterprise-grade paranoia, and you can't afford it anyway. What you need is to stop being the *easiest* target. The overwhelming majority of attacks are opportunistic and automated — bots scanning for default passwords, unpatched bugs, and open ports. A handful of practical steps closes off almost all of that, and they cost you time rather than money.

## Lock the doors that matter

A sensible, achievable security posture for a community network rests on a few pillars:

- **Firewall: allow only what must be allowed.** The default OpenWrt firewall is a good start, but it drifts as you open ports for services. Audit what's actually exposed, close anything you can't justify, and never expose a management interface (LuCI, SSH, the Proxmox UI) directly to the internet — reach those through the VPN instead.
- **Strong, modern WiFi encryption.** Move off a single shared password where you can. Use **WPA3** (or WPA2 at minimum) on devices that support it, and for any network with real users, prefer per-user accounts via RADIUS over one key everyone shares.
- **Keep firmware and software patched.** Unpatched software is the number-one way in. The routers, Proxmox, and your services all ship security fixes; applying them is the highest-value security work you'll ever do. (This is closely tied to the maintenance discipline covered later in this chapter.)
- **Segment the network.** Put IoT devices, guest WiFi, and management traffic on separate VLANs so a compromised camera or a stranger on the guest network can't reach your servers. A flat network means one weak device exposes everything.
- **Harden SSH.** Switch to key-based authentication, disable password login, and don't run SSH on a publicly reachable interface. This single change shuts down the most common automated attack against any Linux box.

## Make it routine, not heroic

Security isn't a project you finish; it's a baseline you maintain. The trap is treating it as a one-time hardening sprint and then never revisiting it. Far better to bake a few habits into how you run the network: a quarterly check of what ports are open, patches applied on a schedule, credentials that aren't shared more widely than they must be, and management access that always goes through the VPN. None of this is glamorous, and that's the point — done quietly and consistently, it dramatically reduces the risk that one bad day turns into a disaster.

!!! tip "Guide reference"
    For a detailed, practical security checklist, see [Guide — Security](../../3-Guide/Security/index.md).
