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
2. The disk image was captured with **Clonezilla** (~4 GB compressed from a 466 GB source disk)
3. The image was **resized** to fit the smallest target disk (238 GB SSD) -- the source ext4 partition was shrunk from 466 GB to 20 GB using `resize2fs` and `parted`, then recaptured with `partclone` (~3.6 GB compressed)
4. A **PXE server** (one of the deployed ThinkPads) served the image to all 9 machines over an isolated Ethernet switch
5. All machines booted from the network and received the image simultaneously

## Lessons Learned

- **Secure Boot must be disabled** on all target machines before PXE boot. The unsigned GRUB binary is silently rejected otherwise -- no error message, just falls through to IPv6 PXE. This was the root cause of hours of debugging.
- **TFTP `--secure` mode breaks symlinks.** Files served via TFTP must be physically inside the TFTP root directory, not symlinked from outside.
- **Partition size matters more than data size.** An image captured from a 466 GB disk cannot be restored to a 238 GB disk, even if the actual data is only 12 GB. The ext4 filesystem scatters blocks across the entire partition, and `partclone` fails when seeking beyond the target disk boundary. The fix is to shrink the filesystem and partition before capturing the image (see [Phase 3 of the guide](../../3-Guide/Laptop-Deployment/index.md#phase-3----resize-the-image-for-smaller-target-disks)).
- **Auto-detect the target disk.** Machines may have SATA (`/dev/sda`) or NVMe (`/dev/nvme0n1`) storage. Use a script that probes for the correct device instead of hardcoding the disk name.
- **DRBL is overkill for this use case.** A simple setup with `isc-dhcp-server` + `tftpd-hpa` + `nfs-kernel-server` + Clonezilla Live is much easier to debug and maintain than a full DRBL deployment.
- **Use `-k1` and `-icds` flags** with `ocs-sr` when deploying to disks of varying sizes. `-k1` proportionally resizes partitions to fill the target disk, and `-icds` skips the disk size check.

<!-- TODO: Photos of the deployment setup, timeline, final state of machines -->
