# *"Where do I put all these files?!"*

Nextcloud is running and people love it. Neighbors upload documents and photos, the cooperative keeps its bookkeeping spreadsheets there, the Kiwix library keeps growing, and Jellyfin now holds a few dozen educational videos. Then Proxmox throws a warning: the host's 128 GB SSD is 95% full. The very success that makes the network valuable is the thing about to break it. When that disk fills completely, services stop writing, databases corrupt, and the platform everyone now depends on falls over.

You need more storage. But "buy a bigger disk" is only the surface of the decision — *how* you add storage determines whether your data is merely *bigger* or actually *safer*.

## The options

There's a spectrum, from quick fixes to proper infrastructure:

- **External HDD** — cheap, plug-and-play, and perfectly fine as a quick way to add capacity or hold a backup. The catch is that it's a single drive on a single cable: convenient, but not something to trust your only copy of important data to.
- **NAS (Network Attached Storage)** — a dedicated storage device that sits on the network and serves files to any machine that needs them. This is the natural home for a growing community deployment: storage becomes a shared resource your Proxmox host, your services, and even desktops can all reach, instead of being trapped inside one server.
- **Multiple drives in RAID** — combining several disks so that the failure of one doesn't lose your data. This is where storage stops being just "space" and starts being **resilience**.

## SSD or HDD?

A practical split, not an either/or: **SSDs** are fast and quiet and belong where speed matters — the Proxmox host's boot drive and the disks your running containers and databases live on. **HDDs** are cheap per terabyte and belong where capacity matters more than speed — bulk file storage, media libraries, and backups. Many setups use both: a small SSD for the system and services, a large HDD (or several) for the data they serve.

## RAID buys redundancy, not backups

This distinction matters enough to state plainly. **RAID** keeps the system running through a *disk* failure: lose one drive in a redundant array and the data is still there on the others while you swap the dead one out. That's valuable — it turns a catastrophe into a maintenance task. But RAID protects against exactly one thing, hardware failure of a drive. It does **not** protect you from a deleted file, a corrupted database, ransomware, fire, or theft, because all of those happen to *all* the mirrored copies at once.

!!! warning "RAID is not a backup"
    A RAID array and a backup solve different problems. RAID keeps you online when a disk dies; a backup gets your data back when something destroys it. You need both — and backups get their own section later in this chapter.

## What to run on a NAS

If you go the NAS route, two open-source platforms dominate and both run on commodity hardware:

- **OpenMediaVault** — lightweight and approachable, comfortable on modest hardware (even a small board or an old PC). A good fit for a typical community deployment.
- **TrueNAS** — more powerful, built around the ZFS filesystem with strong data-integrity guarantees, but hungrier for RAM. Worth it when your storage needs are larger and you want ZFS's checksumming and snapshots.

Either way, the goal is the same: get your growing pile of files off the single SSD that's about to fill up and onto storage that's sized for growth and survives a drive dying.

!!! tip "Guide reference"
    For storage setup instructions, see [Guide — Storage](../../3-Guide/Storage/index.md).
