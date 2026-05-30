# *"Who are all these people on my network?!"*

The network is popular. Too popular. Word spread that there's free WiFi at the community center, and now half the neighborhood connects to it. Students stream video all afternoon. Someone is running downloads that saturate the entire uplink, and everyone else's connection crawls to a halt. You open the list of connected devices and see forty-odd entries with names like "Galaxy-A12" and "iPhone" — and you have no idea who any of them are, which ones belong to the staff who actually need the network, or who's responsible for the traffic that keeps choking it.

The single shared password was fine when "the network" meant a handful of laptops in one office. At neighborhood scale it falls apart. Everyone has the same key, so you can't tell anyone apart, you can't revoke one person without changing the password for *everybody*, and you can't give the clinic's machines priority over someone's video stream. You've built a popular service with no way to manage who uses it or how.

## From one key to many identities

**RADIUS** (Remote Authentication Dial-In User Service) is the standard that turns "one shared password" into "every user has their own account." Combined with WPA2/WPA3-Enterprise on your WiFi, each person logs in with their own username and password instead of a key everyone knows. That one change unlocks real management:

- **Individual accounts** — each user authenticates as themselves, so the network finally knows who's who.
- **Usage tracking (accounting)** — you can see who connected, when, for how long, and how much they transferred. The mystery downloader stops being a mystery.
- **Access control** — limit speeds per account, set time or data quotas, and revoke a single user instantly without disrupting anyone else.
- **Multiple SSIDs with different policies** — a staff network, a student network, and a guest network, each tied to the right group of accounts with the right limits.

It's the difference between an open door and a front desk. The door lets anyone in and remembers nothing. The front desk knows who you are, what you're allowed to do, and can ask you to leave.

## What it costs you

This power comes with real setup. You run a RADIUS server — **FreeRADIUS** is the open-source workhorse — backed by some store of user accounts, and you point your access points at it for authentication. It's more moving parts than a shared password, and it's overkill for a five-laptop office. But once the community depends on the network, individual accounts are what let you keep it fair, fast, and accountable as it grows — and they pair naturally with the captive portal from the previous section, which can hand users off to RADIUS for the actual login.

!!! tip "Guide reference"
    For step-by-step RADIUS setup, see [Guide — RADIUS](../../3-Guide/RADIUS/index.md).
