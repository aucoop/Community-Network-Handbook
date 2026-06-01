# *"Can this network do more than just internet?"*

Once the network is stable, the requests start to change shape. The teachers ask: *"Can we share files between classrooms without emailing them around?"* The clinic asks: *"Can we have a shared calendar everyone can see?"* Someone remembers that the internet uplink drops for hours at a time and asks whether there's a way to keep a copy of Wikipedia locally, so the kids can still look things up when the line is down. None of these are about *internet access*. They're about what the network can *do*.

This is the moment a community network stops being plumbing and becomes a **platform**. The same server you set up for DNS or monitoring can host services that live *inside* your network — services that keep working at full speed even when the internet connection is slow, expensive, or completely down. And because the data never leaves the building, these services are often faster and more private than their cloud equivalents, with no monthly subscription attached.

## A menu of local services

What's worth running depends on what your community needs, but a few services come up again and again:

- **Nextcloud** — the anchor for most deployments. File sharing, shared calendars, contacts, and collaborative document editing — a self-hosted alternative to Google Drive or Dropbox that runs entirely on your own hardware.
- **Kiwix** — offline copies of Wikipedia, educational libraries, and other knowledge collections. Invaluable where the uplink is unreliable: the whole of Wikipedia, available to every classroom whether or not the internet is up.
- **Jellyfin** — a media server for educational videos, recorded lessons, and films, streamed locally without burning uplink bandwidth.
- **LibreSpeed** — a local speed test, so you can measure the network's *internal* performance honestly instead of guessing.
- **Local AI** — a small language model running on your own hardware for offline translation, tutoring, or assistance, with no data leaving the network.

## How to decide what to run

The temptation is to install all of it on day one. Resist that. Every service you run is something you have to maintain, back up, and explain to the next volunteer — and every one consumes RAM, CPU, and disk on hardware that isn't infinite. The better approach is demand-driven:

- **Start with what people actually asked for.** If the teachers want shared files, deploy Nextcloud and nothing else. A service that solves a real, stated problem will be used and valued; one you added speculatively becomes maintenance debt nobody benefits from.
- **Check the cost before you commit.** Some services are featherweight; others (media servers, AI models) want real CPU, RAM, or storage. Match the service to the hardware you have before you promise it.
- **Add one at a time.** Deploy, let people use it, see whether it sticks, and only then move to the next. This keeps the system understandable and the failures isolated.

A word of caution that the next section will pick up: running several of these on one machine without isolation means one bad update can take them *all* down at once. As your service menu grows, *how* you run them starts to matter as much as *which* you run.

!!! tip "Guide reference"
    For Nextcloud setup — the most common first service — see [Guide — Nextcloud](../../3-Guide/Nextcloud/index.md).
