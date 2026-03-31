# Install Proxmox VE on Bare Metal

This guide covers how to install Proxmox VE on a dedicated machine, access the web interface, and apply recommended post-install configuration for community network use.

This guide implements the concept introduced in
[Chapter 2.12 --- Virtualization](../../2-Imaginary-Use-Case/2.12-Virtualization/index.md).

## What You'll Learn

- How to create a bootable USB drive with the Proxmox VE installer
- How to configure disk, network, and hostname settings during installation
- How to access the Proxmox web interface after first boot
- How to disable the enterprise repository and enable free updates
- How to remove the subscription nag popup using the community helper script

## Prerequisites

- A dedicated x86-64 machine with Intel VT-x or AMD-V virtualization support
- A USB drive (at least 2 GB)
- A monitor and keyboard for the initial installation
- A computer on the same LAN to access the web interface after setup
- Internet access on the target machine

!!! info "Hardware recommendations for community networks"
    Mini PCs with Intel N100 or N150 processors offer a good balance of performance, price, and power efficiency for small Proxmox deployments. Plan for at least **8 GB of RAM** per server --- more if you intend to run many VMs or containers. Use an **SSD** for storage; the size depends on your expected workloads. Check the [official Proxmox requirements](https://www.proxmox.com/en/products/proxmox-virtual-environment/requirements) for full details.

## Used Versions

| Software    | Version |
|-------------|---------|
| Proxmox VE  | 9.1.2    |

## Step-by-Step Implementation

### 1. Download the Proxmox VE ISO

1. Go to the [Proxmox VE Downloads page](https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso).
2. Download the latest Proxmox VE ISO Installer (at the time of writing, **Proxmox VE 9.1**).

### 2. Create a bootable USB drive

1. Download [Rufus Portable](https://rufus.ie/) (Windows).
2. Insert your USB drive.
3. Open Rufus and select:
    - **Device:** your USB drive
    - **Boot selection:** the Proxmox VE ISO you downloaded
    - **Partition scheme:** GPT (or MBR if your machine requires legacy BIOS)
4. Click **Start** and wait for the process to finish.

!!! info "Using `dd` on Linux or macOS"
    If you prefer the command line, identify your USB device (e.g., `/dev/sdX`) and run:

    ```bash
    dd bs=1M conv=fdatasync if=./proxmox-ve_*.iso of=/dev/sdX
    ```

    Replace `/dev/sdX` with your actual USB device. Double-check the device name --- `dd` will overwrite the target without confirmation.

### 3. Boot from the USB drive

1. Plug the USB drive into the target machine.
2. Reboot the machine.
3. Press the BIOS key repeatedly during startup to enter the BIOS setup. Common keys are **Esc**, **F2**, **Del**, or **F12** depending on the manufacturer.
4. In the BIOS, navigate to the **Boot** section.
5. Set the USB drive as **Boot Option #1**.
6. Save and exit the BIOS. The machine will restart and boot from the USB drive.

!!! tip "One-time boot menu"
    Many machines support a one-time boot menu (usually **F12** or **F8**) that lets you select the USB drive without changing BIOS settings permanently.

### 4. Install Proxmox VE

1. When the Proxmox installer boot screen appears, select **Install Proxmox VE (Graphical)**.
2. Select the target hard disk for installation:
    - **Filesystem:** `ext4` is the default and works well for most setups.
    - Click **Options** to change the filesystem or configure advanced disk layout.

!!! info "Filesystem choices"
    `ext4` is simple and reliable. `ZFS` offers data integrity checks, snapshots, and built-in RAID, but requires more RAM (roughly 1 GB per TB of storage). For a single-disk community server, `ext4` is the recommended choice.
3. Set the **root password** (minimum 8 characters) and provide an **email address** for system notifications.
4. Configure the network settings:
    - **Hostname:** enter a fully qualified domain name, for example `proxmox01.local`. Avoid spaces and special characters.
    - **IP Address:** assign a static IP that is not already in use on your network, for example `192.168.1.10/24`.
    - **Gateway:** your router's IP address, for example `192.168.1.1`.
    - **DNS Server:** your router's IP (e.g., `192.168.1.1`) or a public DNS server (e.g., `1.1.1.1` or `8.8.8.8`).

!!! warning "Use a static IP"
    Proxmox must be reachable at a predictable address for web management and API access. Always assign a static IP during installation. If you use DHCP, the IP may change after a reboot and you will lose remote access to the web interface.

5. Review the summary and click **Install**.
6. Wait for the installation to complete. When finished, remove the USB drive and let the machine reboot.

!!! tip "Remove the USB drive before reboot"
    If you forget to remove the USB drive, the machine may boot into the installer again instead of the newly installed Proxmox system.

### 5. Access the web interface

1. After the machine reboots, the console will display the Proxmox VE login prompt along with the web interface URL (e.g., `https://192.168.1.10:8006`).
2. On another computer connected to the same network, open a browser and navigate to `https://<your-static-ip>:8006`.
3. Accept the self-signed certificate warning.
4. Log in with:
    - **User name:** `root`
    - **Realm:** `Linux PAM standard authentication`
    - **Password:** the root password you set during installation

!!! tip "Cannot reach the web interface?"
    If the browser cannot connect, verify that your computer is on the same subnet as the Proxmox server. You can also log in directly on the Proxmox console (monitor and keyboard) with the root credentials to check the IP configuration with `ip a`.

### 6. Reserve a static IP in your router

Even though you assigned a static IP during installation, your router's DHCP server does not know about it. Reserve the IP on the router side to prevent address conflicts.

1. Log into your router's administration interface.
2. Find the DHCP or LAN settings section.
3. Add a static lease that maps the Proxmox server's MAC address to its IP address.

!!! info "Why this matters"
    Without a reservation, the router could assign the same IP to another device. A static lease ensures the Proxmox server's IP is never given to anything else on the network. Each router brand has a different interface for this --- consult your router's documentation.

### 7. Run the post-install helper script

A fresh Proxmox installation is configured to use the Enterprise repository, which requires a paid subscription. For community network deployments without a subscription, you need to switch to the free No-Subscription repository and remove the subscription reminder popup.

The [Proxmox VE Helper Scripts](https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install) project provides a script that automates this configuration.

1. Connect to the Proxmox server via SSH or use the web shell (**Datacenter -> your node -> Shell**):

    ```bash
    ssh root@<your-static-ip>
    ```

2. Run the post-install helper script:

    ```bash
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/post-pve-install.sh)"
    ```

3. Follow the interactive prompts:
    - **Correct Proxmox VE sources?** --- Yes
    - **Disable Enterprise repository?** --- Yes
    - **Enable No-Subscription repository?** --- Yes
    - **Correct Ceph package sources?** --- Yes
    - **Add the pve-no-subscription repository?** --- Yes
    - **Disable the subscription nag?** --- Yes
    - Enable or disable other optional repositories based on your needs.

4. Reboot the server when the script finishes:

    ```bash
    reboot
    ```

5. Log back into the web interface and verify:
    - The Enterprise repository is disabled under **Datacenter -> your node -> Updates -> Repositories**.
    - The No-Subscription repository is enabled.
    - The subscription popup no longer appears at login.

??? tip "Manual alternative --- configure repositories without the script"
    If you prefer not to run a third-party script, you can configure the repositories manually through the web interface:

    1. Go to **Datacenter -> your node -> Updates -> Repositories**.
    2. Select the `pve-enterprise` repository and click **Disable**.
    3. Click **Add**, select **No-Subscription**, and click **Add**.
    4. Go to **Datacenter -> your node -> Updates**, click **Refresh**, then **Upgrade** to apply available updates.

??? tip "Manual alternative --- remove the subscription popup"
    If you did not use the helper script and the subscription popup still appears at login:

    1. SSH into the Proxmox server.
    2. Back up the web UI JavaScript file:

        ```bash
        cp /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js.backup
        ```

    3. Edit the file and find the line containing `"No valid subscription"`. Comment it out or remove the surrounding check block.
    4. Restart the web proxy:

        ```bash
        systemctl restart pveproxy
        ```

    !!! warning
        This change will be overwritten by future Proxmox updates. You will need to reapply it after each update, which is why the helper script is the recommended approach.

## References
- YouTube: "Let's install Proxmox 8.3 in 2025: From Scratch. Spelled out." -- <https://youtu.be/kqZNFD0JNBc?si=FWxcrOD6rYh8Keas>
- YouTube: "Proxmox Beginner’s Guide: Everything You Need to Get Started" -- <https://youtu.be/lFzWDJcRsqo?si=zuQB9QXDOdOrwhuV>
- Proxmox VE System Requirements -- <https://www.proxmox.com/en/products/proxmox-virtual-environment/requirements>
- Proxmox VE ISO Downloads -- <https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso>
- Proxmox VE Helper Scripts (Community Edition) -- <https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install>
- Rufus --- Bootable USB Creator -- <https://rufus.ie/>

## Revision History

| Date       | Version | Changes                | Author       | Contributors                    |
|------------|---------|------------------------|--------------|---------------------------------|
| 2026-03-31 | 1.0     | Initial guide creation | Jaime Motje  | Maria Jover, Sergio Gimenez    |
