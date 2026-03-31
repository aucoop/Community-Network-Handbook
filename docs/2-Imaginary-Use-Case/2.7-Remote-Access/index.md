# *"Something broke and I'm 500 km away"*

You built the network during a two-week visit. You configured every router by hand, set up the monitoring, got the DNS running, and left feeling confident that things were solid. Now you're back home, 500 km away, and Zabbix just sent you an alert: a router in the school building needs reconfiguring. The teacher on site can reboot it, but she can't open a terminal and type commands. You need to do it yourself --- remotely.

The problem is that your community network sits behind NAT. Every device has a private IP address like `192.168.1.x`, invisible from the outside internet. You can't just SSH into `192.168.1.35` from your apartment --- the public internet has no idea that address exists. And even if the ISP gave you a public IP today, it will probably change tomorrow. You need a way to **always** reach your network, reliably, regardless of where you are or what the ISP does.

This is what a **VPN** (Virtual Private Network) solves. A VPN creates an encrypted tunnel between your laptop and the community network. Once connected, it's as if you were physically there --- you can SSH into routers, open the LuCI web interface, check Zabbix dashboards, and manage everything exactly as you would sitting in front of the devices. Except you're on your couch.

## Why WireGuard?

There are many VPN technologies. OpenVPN has been the default for years, but it's complex to configure, CPU-heavy (a real problem on low-power routers), and its performance suffers under high latency --- exactly the conditions you find in rural deployments.

**WireGuard** is the modern alternative. It is built into the Linux kernel (and therefore into OpenWrt), uses state-of-the-art cryptography, and its entire codebase is roughly 4,000 lines --- compared to OpenVPN's hundreds of thousands. In practice this means:

- **Faster connections**: WireGuard establishes tunnels almost instantly. OpenVPN can take seconds.
- **Lower overhead**: critical when your routers have limited CPU and RAM.
- **Simpler configuration**: a WireGuard tunnel is defined by a short config file with public keys and endpoints, not pages of certificate management.
- **Roaming-friendly**: if your IP changes (mobile data, ISP restart), WireGuard reconnects silently.

The trade-off is that WireGuard by itself is just a tunnel --- it doesn't manage keys, distribute configurations, or tell nodes about each other. If you have two devices, that's fine: you generate a key pair on each, exchange public keys, and done. But when you have ten routers, a server, and your laptop? You need something to **orchestrate** all those tunnels.

## Netmaker: WireGuard with a control plane

**Netmaker** is an open-source platform that manages WireGuard networks from a central dashboard. You install the Netmaker server on a cheap VPS (Virtual Private Server) with a public IP, and then install a lightweight agent called **Netclient** on each device you want in the network. Netclient handles key generation, configuration, and keeps the WireGuard tunnels up to date automatically.

The VPS acts as a coordination point: it tells each node about the others and distributes the WireGuard configurations. But the actual traffic flows **directly between nodes** --- your SSH session from home to the school router does not bounce through the VPS. This is a mesh topology: every node can reach every other node directly through encrypted WireGuard tunnels.

## More than just remote access

Once the VPN mesh is running, you get more than just remote management. You can set up **egress routes** so that any device on the VPN can reach the entire LAN behind a router, not just the router itself. If you need to access the Nextcloud server sitting on `192.168.1.50` behind the community center router, the VPN makes that possible without exposing anything to the public internet.

You can also use Netmaker's **Remote Access Gateway** feature to let non-technical users connect temporarily --- for example, a volunteer visiting a different site who needs to reach the monitoring dashboard. They get a WireGuard config file, connect, and they're in. When they're done, you revoke access from the dashboard.

This is the piece that turns a collection of isolated sites into a **single, manageable network**. Without it, every time something breaks at a site you can't physically visit, you're stuck asking someone on the ground to describe what they see on a screen. With it, you're there in seconds.

!!! tip "Guide reference"
    For step-by-step VPN setup, see the [VPN guides](../../3-Guide/VPN/index.md):

    - [Install Netmaker on a VPS](../../3-Guide/VPN/Netmaker-VPS.md) --- deploy the Netmaker server that will coordinate your VPN network.
    - [Install Netclient on OpenWrt](../../3-Guide/VPN/Netclient-OpenWrt.md) --- enroll an OpenWrt router into the VPN and configure LAN-to-VPN routing.

<!-- TODO: Add diagram showing egress routing concept, expand on Remote Access Gateway use cases -->
