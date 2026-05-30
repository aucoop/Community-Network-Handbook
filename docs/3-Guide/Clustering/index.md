# Create and Manage a Proxmox Cluster

This guide covers how to create a Proxmox VE cluster from two or more nodes, configure quorum for a two-node setup using a QDevice, and handle common cluster operations like node removal.

This guide implements the concept introduced in [Chapter 2.14 -- Clustering](../../2-Imaginary-Use-Case/2.14-Clustering/index.md).

## What You'll Learn

- How to create a Proxmox VE cluster and join additional nodes
- How quorum works and why two-node clusters need special attention
- How to set up a QDevice to provide a tie-breaking vote
- How to ensure network bridge consistency across nodes
- How to remove a node from a cluster or dissolve the cluster entirely

## Prerequisites

- Two or more machines running Proxmox VE (same major version on all nodes)
- Network connectivity between all nodes (ideally a dedicated cluster network)
- Root SSH access between nodes
- For QDevice: one additional lightweight Linux machine (Raspberry Pi, LXC container, or small VM **outside** the cluster)

## Used Versions

| Software       | Version              |
|----------------|----------------------|
| Proxmox VE     | 8.x                 |
| Corosync       | 3.x (ships with PVE) |
| corosync-qnetd | 3.x (on QDevice host) |

## Step-by-Step Implementation

### 1. Prepare the nodes

1. Ensure all nodes run the same Proxmox VE major version.
2. Set a unique hostname on each node. The hostname must be resolvable from every other node.
3. Verify that each node can reach the others via SSH:

    ```bash
    ssh root@<other-node-ip> hostname
    ```

4. If nodes have different CPU models, plan to set the CPU type to `x86-64-v2-AES` (or another common baseline) for any VMs you want to live-migrate. The `Host` CPU type only works when all nodes share the same CPU.

!!! info "Empty node requirement"
    When a node joins an existing cluster, its local configuration (`/etc/pve`) is replaced by the cluster configuration. Any VMs or containers defined only on that node's local config will be lost. Always join from a fresh or empty node, or back up first.

---

### 2. Create the cluster on the first node

1. Open the Proxmox web UI on the node that will be the first cluster member.
2. Navigate to **Datacenter --> Cluster --> Create Cluster**.
3. Enter a cluster name (e.g., `community-cluster`).
4. Select the network link for cluster communication. If you have a dedicated cluster network interface, choose it here.
5. Click **Create**.

Alternatively, create the cluster from the command line:

```bash
pvecm create community-cluster
```

To specify a dedicated cluster network:

```bash
pvecm create community-cluster --link0 10.10.10.1
```

!!! info "Cluster network"
    The cluster link carries Corosync traffic (heartbeat, quorum votes, configuration sync). A dedicated network or VLAN avoids contention with VM traffic. If you only have one network, that works too -- Corosync traffic is lightweight.

---

### 3. Join the second node to the cluster

1. On the **first node** (the one where you created the cluster), navigate to **Datacenter --> Cluster**.
2. Click **Join Information** and copy the displayed join string.
3. On the **second node**, navigate to **Datacenter --> Cluster --> Join Cluster**.
4. Paste the join information.
5. Enter the **root password** of the first node.
6. Select the correct network link if prompted.
7. Click **Join**.

Alternatively, from the second node's command line:

```bash
pvecm add <first-node-ip>
```

You will be prompted for the first node's root password.

!!! warning "Irreversible merge"
    Joining a cluster overwrites the joining node's `/etc/pve` configuration. If the second node already has VMs or containers, back up their configurations before joining.

---

### 4. Verify cluster status

1. On any node, run:

    ```bash
    pvecm status
    ```

2. Confirm the output shows all expected nodes and `Quorate: Yes`.
3. List individual nodes and their vote counts:

    ```bash
    pvecm nodes
    ```

4. In the web UI, navigate to **Datacenter --> Cluster** and verify all nodes appear with a green status.

---

### 5. Understand quorum (and why 2 nodes are risky)

1. Proxmox uses Corosync's **votequorum** system. Each node holds 1 vote.
2. The cluster requires a **majority** of total votes to operate (this is called having quorum).
3. With 3 nodes: losing 1 leaves 2 out of 3 votes -- quorum is maintained.
4. With 2 nodes: losing 1 leaves 1 out of 2 votes -- **no majority, no quorum**. The surviving node freezes HA operations and refuses to start or migrate VMs.

!!! danger "Emergency override"
    If you are stuck with a single surviving node and no QDevice, you can temporarily force quorum:

    ```bash
    pvecm expected 1
    ```

    This tells Corosync to accept 1 vote as sufficient. **This is a temporary fix.** It does not persist across reboots, and running a cluster in this state long-term risks split-brain if the other node comes back up independently.

---

### 6. Set up a QDevice for 2-node quorum

A QDevice is a lightweight external voter that gives your two-node cluster the third vote it needs to survive a single node failure.

**On the QDevice host (Debian/Ubuntu machine, Raspberry Pi, or LXC container):**

1. Install the QDevice network daemon:

    ```bash
    apt update
    apt install corosync-qnetd
    ```

2. Ensure the `corosync-qnetd` service is running:

    ```bash
    systemctl enable --now corosync-qnetd
    ```

3. Ensure root SSH login is enabled (at least temporarily) so the Proxmox node can push certificates:

    ```bash
    # In /etc/ssh/sshd_config, set:
    # PermitRootLogin yes
    systemctl restart sshd
    ```

**On each Proxmox node:**

4. Install the QDevice client package:

    ```bash
    apt update
    apt install corosync-qdevice
    ```

**Run the setup from one Proxmox node:**

5. Execute the QDevice setup command, pointing to the QDevice host's IP:

    ```bash
    pvecm qdevice setup <qdevice-ip>
    ```

6. Accept the SSH fingerprint when prompted and enter the QDevice host's root password.
7. Wait for the setup to complete. You should see `Done` at the end.

**Verify the QDevice:**

8. Check cluster status:

    ```bash
    pvecm status
    ```

9. Confirm the output now shows 3 expected votes (1 per node + 1 for QDevice) and `Quorate: Yes`.

!!! tip "QDevice placement"
    The QDevice host must **not** be a member of the Proxmox cluster. A Raspberry Pi, a small VM on a different hypervisor, or an LXC container on a separate machine all work. The only requirement is network connectivity to the cluster nodes on port **5403/tcp**.

---

### 7. Match network bridges across nodes

1. On each node, list the existing network bridges:

    ```bash
    cat /etc/network/interfaces
    ```

2. Ensure every node has the **same bridge names** (e.g., `vmbr0`, `vmbr1`). Proxmox maps a VM's network interface to a bridge by name. If `vmbr0` exists on Node A but not on Node B, migrating a VM that uses `vmbr0` to Node B will fail.
3. If bridges differ, edit `/etc/network/interfaces` on the mismatched node to rename or create the missing bridges.
4. Apply the network changes:

    ```bash
    ifreload -a
    ```

!!! info "Bridge purpose can differ"
    The bridges must share the same **names**, but they do not need identical physical configurations. For example, `vmbr0` on Node A might use `enp3s0` while `vmbr0` on Node B uses `eno1`. What matters is that the bridge name exists so the VM config is valid on both sides.

---

### 8. Remove a node or dissolve the cluster

#### Remove a single node

1. Migrate all VMs and containers off the node you want to remove.
2. Power off the node to be removed.
3. From a remaining cluster node, delete the node:

    ```bash
    pvecm delnode <node-name>
    ```

4. Clean up any leftover configuration files:

    ```bash
    rm -rf /etc/pve/nodes/<node-name>
    ```

5. Verify with `pvecm status` and `pvecm nodes`.

#### Dissolve the cluster entirely (reset a node to standalone)

If you need to completely remove cluster configuration from a node and return it to standalone mode:

1. Stop cluster services:

    ```bash
    systemctl stop pve-cluster corosync
    ```

2. Start the cluster filesystem in local mode:

    ```bash
    pmxcfs -l
    ```

3. Remove cluster configuration files:

    ```bash
    rm /etc/corosync/*
    rm /etc/pve/corosync.conf
    ```

4. Kill the local-mode filesystem and restart the cluster service:

    ```bash
    killall pmxcfs
    systemctl start pve-cluster
    ```

5. Reboot the node:

    ```bash
    reboot
    ```

6. After reboot, verify the node is standalone:

    ```bash
    pvecm status
    ```

    You should see a single-node status or an error indicating no cluster exists.

!!! warning "Data safety"
    Dissolving a cluster does not delete VMs or container data on local storage. However, any shared/remote storage configuration and HA groups will be lost. Back up your VM configurations from `/etc/pve/qemu-server/` and `/etc/pve/lxc/` before dissolving.

---

## References

- Proxmox VE Cluster Manager documentation -- <https://pve.proxmox.com/pve-docs/chapter-pvecm.html>
- Proxmox VE Wiki: Cluster Manager -- <https://pve.proxmox.com/wiki/Cluster_Manager>
- pvecm man page -- <https://pve.proxmox.com/pve-docs-8/pvecm.1.html>

## Revision History

| Date       | Version | Changes                | Author | Contributors |
|------------|---------|------------------------|--------|--------------|
| 2026-04-02 | 1.0     | Initial guide creation | JML    |              |
