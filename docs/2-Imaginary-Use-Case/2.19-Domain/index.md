# *"I want people to find us from outside"*

Your network has grown into something real. There's a website you built, a Nextcloud instance the community relies on, maybe a public status dashboard. But there's a catch: all of it lives *inside* the network. To reach any of it, you either have to be on the local WiFi or connected through the VPN. A funder you want to impress can't just type an address and see what you've built. A volunteer in another city can't reach the dashboard. From the outside world's point of view, your network is invisible.

The bridge to the outside is a **domain name** — something like `mynetwork.org`. It's the difference between an address only insiders know (`192.168.1.50`, reachable only from within) and a public identity anyone on the internet can find and trust.

## What a domain unlocks

A domain is cheap — often under €15 a year — and it's the foundation for a whole set of capabilities:

- **A public identity.** People can find you, link to you, and remember you. `mynetwork.org` is something you can print on a flyer; an IP address is not.
- **Real email.** `info@mynetwork.org` instead of a personal Gmail account. It signals that the project is an organization, not one person's side project — which matters when you're talking to funders and partners.
- **Free HTTPS.** With a domain you can get free SSL/TLS certificates from **Let's Encrypt**, so your services are served over secure, padlock-in-the-browser HTTPS instead of scary "not secure" warnings.
- **Structured subdomains.** Point different names at different services: `cloud.mynetwork.org` for Nextcloud, `status.mynetwork.org` for the dashboard, `www.mynetwork.org` for the site. One domain organizes your whole public presence.

## How the pieces fit

Getting from "I bought a domain" to "people can reach my service" comes down to a few moving parts:

- **A registrar** — the company you buy the domain from and where you manage it. Pick a reputable one; the cheapest first-year deal sometimes hides expensive renewals or awkward management.
- **DNS records** — the settings that tell the internet where your domain points. The ones you'll use most are **A records** (name → IP address, e.g. `cloud.mynetwork.org` → your public IP), **CNAME records** (one name as an alias for another), and **MX records** (where email for the domain is delivered).
- **A way to handle a changing IP.** Many community networks sit behind a connection whose public IP changes without warning. A static A record would break every time it did. **Dynamic DNS (DDNS)** solves this: a small client updates the DNS record automatically whenever the IP changes, so your domain keeps pointing to the right place. (If you publish services through your VPS or VPN instead, you may point the domain there and sidestep the changing-IP problem entirely.)

A domain is a small purchase with an outsized effect: it's the moment your private community network gains a public face — and the prerequisite for the website that comes next.

!!! tip "Guide reference"
    For domain registration and DNS record setup, see [Guide — Domain](../../3-Guide/Domain/index.md).
