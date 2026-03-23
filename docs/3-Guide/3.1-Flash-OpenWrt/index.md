# Flash OpenWrt

This section contains step-by-step instructions for installing OpenWrt on specific router models.

!!! warning "Check compatibility first"
    Not every router supports OpenWrt. Always check the [OpenWrt Table of Hardware](https://openwrt.org/toh/start) before purchasing.

## Supported Models

The following guides are available:

- [Cudy WR3000E](Cudy-WR3000E.md)
- [Debrick a Router](Debrick.md)

## Troubleshooting

### Can't reach the router's default IP

If you cannot access the router's web interface (e.g., `192.168.10.1`, `192.168.1.1`, or whatever the manufacturer sets), try the following:

1. **Use Ethernet, not Wi-Fi.** Connect your computer directly to one of the router's LAN ports with a cable.
2. **Disable Wi-Fi on your computer.** An active Wi-Fi connection can cause routing conflicts that prevent your browser from reaching the router.
3. **Check your IP address.** Confirm your computer received an IP in the router's subnet. Run `ip a` (Linux) or `ipconfig` (Windows) and look for an address in the same range as the router (e.g., `192.168.10.x`).
4. **Try a different cable or LAN port.** Faulty cables and dead ports are more common than you'd think.
5. **Power-cycle the router.** Unplug it, wait 10 seconds, plug it back in, and wait 60 seconds before trying again.
6. **Factory reset the router.** Hold the reset button for 10+ seconds to restore factory defaults. This is useful if a previous configuration changed the default IP.
7. **Check your browser.** Make sure it isn't routing traffic through a proxy or VPN.

!!! info "Work in Progress"
    More router guides will be added as we test and document additional models.
