# Namibia -- Labdoo Laptop Deployment

!!! info "Work in Progress"
    This case study is being written. It documents a real laptop deployment for a community project in Namibia using the [Labdoo](https://www.labdoo.org/) platform.

## Context

[AUCOOP](https://aucoop.upc.edu) refurbishes donated laptops through the [Labdoo](https://www.labdoo.org/) project and ships them to communities in need. For a 2026 deployment to Namibia, 9 refurbished Lenovo ThinkPads (7x T460, 2x X260) needed to be provisioned with Linux Mint 22.3 and a standard user environment.

Setting up 9 machines manually would take most of a day. Using PXE network boot and Clonezilla, the same task was completed in about an hour.

## Hardware

| Model          | CPU          | RAM    | Storage         | Quantity |
|----------------|--------------|--------|-----------------|----------|
| Lenovo T460    | Intel i5-6200U | 8 GB DDR4 | ~466 GB HDD | 7        |
| Lenovo X260    | Intel i5-6200U | 8 GB DDR4 | ~238 GB SSD / ~466 GB HDD | 2 |

## Deployment Method

The deployment followed the [Laptop Deployment Guide](../../3-Guide/Laptop-Deployment/index.md):

1. One laptop was configured as the **golden master** (Linux Mint 22.3, `aucoop` user, pre-installed software)
2. The disk image was captured with **Clonezilla** (~4 GB compressed)
3. A **PXE server** (ThinkPad X270) served the image to all 9 machines over an isolated Ethernet switch
4. All machines booted from the network and received the image simultaneously

## Lessons Learned

- **Secure Boot must be disabled** on all target machines before PXE boot. The unsigned GRUB binary is silently rejected otherwise -- no error message, just falls through to IPv6 PXE.
- **TFTP `--secure` mode breaks symlinks.** Files served via TFTP must be physically inside the TFTP root directory, not symlinked from outside.
- **The golden master image must fit on the smallest disk** in the batch. One machine had a 238 GB SSD while the rest had 466 GB HDDs.
- **DRBL is overkill for this use case.** A simple setup with `isc-dhcp-server` + `tftpd-hpa` + `nfs-kernel-server` + Clonezilla Live is much easier to debug and maintain than a full DRBL deployment.

<!-- TODO: Photos of the deployment setup, timeline, final state of machines -->
