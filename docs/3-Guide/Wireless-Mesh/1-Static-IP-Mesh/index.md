# OpenWrt 802.11s Wireless Mesh Setup (Iteration 1 — Static IP)

This guide walks you through the **first iteration** of a wireless mesh deployment: configuring an 802.11s wireless mesh backhaul between two OpenWrt routers using the LuCI web interface, plus a shared 2.4 GHz access point for end users. Each satellite is assigned a unique static LAN IP by hand.

This guide implements the concepts introduced in
[Chapter 2.2 — Expanding Coverage](../../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/index.md), in particular [Wired vs Wireless](../../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/2.2.3-Wired-vs-Wireless.md).

!!! tip "Next iteration: DHCP-based mesh"
    Once this static-IP mesh is up and running, the recommended next step is to follow the [DHCP-based Mesh guide](../2-DHCP-Mesh/index.md) to centralize IP management on the main router. The two guides are designed to be done in sequence — see the [Wireless Mesh overview](../index.md) for the full path.

!!! note "Other mesh setups possible"
    This is not the only way to set up a wireless mesh with OpenWrt. This guide focuses on a simple, beginner-friendly setup using LuCI that is suitable for most community network use cases. It uses the 5 GHz band for the mesh backhaul and 2.4 GHz for the access point, but other configurations are possible depending on your hardware capabilities and coverage needs.

## What You'll Learn

- How to swap the default Wi-Fi package for one that supports 802.11s mesh
- How to turn a secondary router into a "dumb AP" so it does not conflict with the main router
- How to create a 5 GHz mesh backhaul link between two routers
- How to configure a shared 2.4 GHz access point for seamless roaming

## Prerequisites

- Two OpenWrt routers with dual-band radios (2.4 GHz + 5 GHz). Could be also done only with 2.4 GHz.
- Both routers already flashed with OpenWrt (see [Flash OpenWrt](../../Flash-OpenWrt/index.md))
- LuCI web interface accessible on both routers
- Both routers on the same LAN subnet (or reachable for initial configuration)
- A computer with a web browser and an Ethernet cable

!!! warning "Perform the package swap on both routers"
    Every step marked "on both routers" must use **identical** settings on each device. A mismatch in mesh ID, channel, or encryption key will prevent the link from forming.

## Used Versions

| Software       | Version          |
|----------------|------------------|
| OpenWrt        | 25.12.1          |
| wpad-mesh-wolfssl | 2025.08.26~ca266cc2-r1	    |
| Router model   | Cudy WR3000E v1  |


!!! note "Your versions may work as well"
    This guide was tested with the above versions, but other recent versions of OpenWrt and the wpad-mesh package should work similarly.

    [**You can open an issue**](https://github.com/aucoop/Community-Network-Handbook/issues/new) if you encounter any problems with your versions.


## Step-by-Step Implementation

### 1. Set the LAN IP address

Each router needs a unique IP on your subnet so they do not conflict.

1. Go to **Network → Interfaces** and click **Edit** on the **LAN** interface.
2. Change the **IPv4 address** to fit your main subnet. For example, if the main router is `192.168.70.1`, set the secondary router to `192.168.70.3`.

    ![LuCI LAN interface showing the IPv4 address field set to a new IP](images/Wireless-Mesh-set-lan-ip.webp){ width="600" }

3. Click **Save & Apply**. You will need to reconnect to the router using the new IP address.
4. On the **secondary router only**, set the **IPv4 gateway** to the main router's IP (e.g., `192.168.70.1`) in the same **LAN** interface edit screen.
5. On the **secondary router only**, switch to the **Advanced Settings** tab and add the main router's IP (e.g., `192.168.70.1`) as a **custom DNS server**.
6. Click **Apply Unchecked** --> Red option. If you only click "Save & Apply" most probably the router will rollback the changes you've made. Reconnect to the router using the new IP address.

!!! info "Why configure gateway and DNS on the secondary router?"
    The secondary router itself needs internet access for management tasks like package updates and NTP sync. Pointing its gateway and DNS to the main router gives it that connectivity.

### 2. Remove the default Wi-Fi package

OpenWrt ships with `wpad-basic-mbedtls` (or a similar variant), which does not support 802.11s mesh. You must replace it with the mesh-capable version.

1. Navigate to **System → Software**.
2. Click **Update lists** to refresh the package index.
3. Filter for `wpad-basic`.
4. Find your installed version (e.g., `wpad-basic-mbedtls`) and click **Remove**.

    ![LuCI Software page showing wpad-basic-mbedtls selected for removal](images/Wireless-Mesh-remove-wpad-basic.webp){ width="600" }

!!! warning "Wait for the removal to finish"
    Do not proceed until the removal completes. Installing the new package while the old one is still present can cause LuCI errors or a broken Wi-Fi stack.

### 3. Install the mesh-capable Wi-Fi package

1. Still in **System → Software**, filter for `wpad-mesh`.
2. Find the matching variant (e.g., `wpad-mesh-wolfssl`) and click **Install**.

    ![LuCI Software page showing wpad-mesh-wolfssl ready to install](images/Wireless-Mesh-install-wpad-mesh.webp){ width="600" }

3. Navigate to **System → Reboot** and restart the router.
4. Repeat steps 1 through 3 on the second router before continuing.

!!! tip "Verify the package is active"
    After rebooting, go back to **System → Software** and confirm that `wpad-mesh-wolfssl` (or your chosen variant) appears in the installed list and that `wpad-basic-*` is gone.

### 4. Disable DHCP on the secondary router

The secondary router must act as a "dumb AP" so it does not hand out its own IP addresses or compete with the main router's DHCP server.

1. On the **secondary router only**, go to **Network → Interfaces** and click **Edit** on the **LAN** interface.
2. Scroll down to the **DHCP Server** section.
3. Check the box **Ignore interface** to disable DHCP on this device.

    ![LuCI DHCP Server section with the Ignore interface checkbox enabled](images/Wireless-Mesh-disable-dhcp.webp){ width="600" }

4. Click **Save & Apply**.

!!! info "Why disable DHCP?"
    Two DHCP servers on the same network will hand out conflicting leases, causing intermittent connectivity for all clients. Only the main router should run DHCP.

### 5. Configure the 5 GHz mesh backhaul

This is the wireless link that connects the two routers together. The settings must be **identical** on both devices.

1. On each router, go to **Network → Wireless**.
2. Find the radios (e.g. `radio0`, `radio1`) and remove any default Wi-Fi networks attached to them.

    ![LuCI Wireless page with the default 5 GHz network being removed](images/Wireless-Mesh-remove-default-wifi.webp){ width="600" }

3. Click **Add** on the 5 GHz radio to create a new wireless interface.

    ![LuCI showing the Add button on the 5 GHz radio](images/Wireless-Mesh-add-5ghz-interface.webp){ width="600" }

4. Configure the **Device Configuration** section:

    - **Channel**: A fixed channel (e.g., **44**). Do **not** use Auto.
    - **Width**: **20 MHz** or **40 MHz**. Narrower channels penetrate walls better.

5. Configure the **Interface Configuration** section:

    - **Mode**: **802.11s**
    - **Mesh ID**: `School_Backhaul` (must match exactly on both routers)
    - **Network**: check the box for **lan**

    ![LuCI radio and interface configuration for the 5 GHz mesh backhaul](images/Wireless-Mesh-radio-configuration.webp){ width="600" }

6. Configure the **Wireless Security** section:

    - **Encryption**: **WPA3-SAE**
    - **Key**: a strong password, identical on both routers

    ![LuCI wireless security configuration for the mesh interface](images/Wireless-Mesh-mesh-security.webp){ width="600" }

7. Click **Save & Apply** on both routers.
8. Check the **Network → Wireless** page — a **Tx/Rx rate** appearing on the mesh interface and an entry under **Associated Stations** confirm the link is up.

    ![LuCI Wireless page showing the mesh peer listed under Associated Stations](images/Wireless-Mesh-associated-stations.webp){ width="600" }

!!! tip "No link forming?"
    Double-check that the channel, mesh ID, encryption type, and key are identical on both routers. Also ensure both devices are within radio range and that no DFS channels are causing radar detection delays.

### 6. Configure the 2.4 GHz access point (fronthaul)

This is the Wi-Fi network that end users will connect to. Configure it on **both** routers so users can roam seamlessly between them.

1. Go to **Network → Wireless**.
2. Find the **2.4 GHz radio** and click **Add** (or **Edit** if a default network exists).
3. Configure the **Device Configuration** section:

    - **Channel**: **Auto**, or a fixed non-overlapping channel (**1**, **6**, or **11**)
    - **Transmit Power**: Default or Medium (approximately 15–18 dBm)

4. Configure the **Interface Configuration** section:

    - **Mode**: **Access Point**
    - **ESSID**: `School_Student_WiFi`
    - **Network**: check the box for **lan**

    ![LuCI 2.4 GHz interface configuration for the student access point](images/Wireless-Mesh-2ghz-ap-config.webp){ width="600" }

5. Configure the **Wireless Security** section:

    - **Encryption**: **WPA2-PSK** (best compatibility with older student devices)
    - **Key**: the shared password for students

    ![LuCI 2.4 GHz wireless security settings](images/Wireless-Mesh-2ghz-ap-security.webp){ width="600" }

6. Click **Save & Apply**.

!!! info "Seamless roaming between access points"
    For users to move between coverage areas without re-entering the password, the **ESSID**, **Encryption**, and **Key** must be identical on the 2.4 GHz AP of all routers. Devices will automatically switch to the strongest available signal.

## References

- OpenWrt Documentation -- Mesh / 802.11s: <https://openwrt.org/docs/guide-user/network/wifi/mesh/80211s>
- Video: "OpenWrt 802.11s Mesh Setup" — <https://www.youtube.com/watch?v=vVoZppb_FR0>

## Revision History

| Date       | Version | Changes                | Author           | Contributors |
|------------|---------|------------------------|------------------|--------------|
| 2026-03-24 | 1.0     | Initial guide creation | Maria Jover        |Jaime Motjé, Sergio Giménez              |
