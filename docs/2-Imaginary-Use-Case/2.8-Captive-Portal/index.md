# *"People connect and don't even know whose network this is"*

Someone sits down in the courtyard, opens their phone, taps the WiFi network, and... that's it. They're online. No welcome message, no terms of use, no hint of who's providing the service or why. To them it's just "free WiFi," indistinguishable from the signal leaking out of a café. They have no idea they're using a network the community built, paid for, and maintains — and that ignorance quietly undermines everything you're trying to do. People don't value, fund, or protect what they don't know exists.

A **captive portal** fixes that first impression. It's the splash page that appears the moment someone joins the WiFi — the same kind you've seen in hotels and airports, where you can't browse until you've clicked through a welcome screen. For a community network, that screen is far more than a formality. It's the network introducing itself.

## What a portal does for you

A captive portal earns its place by doing several jobs at once:

- **It welcomes users and explains the project.** A sentence or two — "This network is run by and for the community of X" — turns anonymous bandwidth into a recognizable service with a face and a story.
- **It shows terms of use.** A short, plain-language acceptable-use policy that people acknowledge before connecting sets expectations and gives you a clear footing if someone abuses the network.
- **It can require basic authentication.** That might be as light as accepting the terms, or as structured as a shared password or a name and email — enough to discourage drive-by abuse without turning the network into a bureaucracy.
- **It carries your identity.** Your logo, your colors, the names of the partners and funders who made it possible. Visibility is not vanity here — it's how the project attracts the volunteers, donations, and goodwill that keep it alive. The portal is the most-seen page on your whole network.

## A note on scope

A captive portal is about *presentation and light gatekeeping*, not strong security. It's the front-desk greeting, not the lock on the door — it makes the network legible and accountable, and gently controls who walks in. When you need genuine per-user accounts, usage tracking, and real access control, that's a different tool (RADIUS, covered in the next section), and the two work well together: the portal greets, the authentication backend decides.


!!! tip "Guide reference"
    For step-by-step captive portal setup, see [Guide — Captive Portal](../../3-Guide/Captive-Portal/index.md).
