# Migrate VMs and Containers Between Proxmox Cluster Nodes

This guide covers how to move virtual machines and LXC containers between nodes in a Proxmox VE cluster, including live migration, offline migration, storage migration, and bulk operations.

This guide implements the concept introduced in [Chapter 2.14 -- Clustering](../../2-Imaginary-Use-Case/2.14-Clustering/index.md).

## What You'll Learn

- How to live-migrate a running VM to another node with zero downtime
- How to perform offline migrations for VMs and LXC containers
- How to move disks between storage backends using `qm move-disk` and `pct move-volume`
- How to evacuate all workloads from a node before maintenance
- How to troubleshoot common migration errors

## Prerequisites

- A Proxmox VE cluster with two or more nodes (see [Create and Manage a Proxmox Cluster](Create-Cluster.md))
- Network bridge names must be consistent across all nodes (covered in the cluster guide linked above)
- Root SSH access between all cluster nodes
- For live migration: shared storage (e.g., Ceph, NFS, iSCSI) or willingness to use the `--with-local-disks` flag
- QEMU Guest Agent installed inside VMs (recommended for clean live migration)

## Used Versions

| Software   | Version |
|------------|---------|
| Proxmox VE | 9.1.2  |

## Step-by-Step Implementation

### 1. Live-migrate a running VM (online migration)

Live migration moves a running VM to another node with minimal downtime. The VM stays running throughout the process.

!!! info "Requirements for live migration"
    Live migration requires one of the following:

    - **Shared storage** (Ceph, NFS, iSCSI, GlusterFS) accessible from both source and target nodes.
    - **Local storage with `--with-local-disks`**, which copies the disk over the network during migration.

    Additionally, all network bridges referenced by the VM must exist on the target node, and the CPU type must be compatible. If nodes have different CPUs, set the VM CPU type to `x86-64-v2-AES` or another common baseline instead of `host`.

**Via the web UI:**

1. Navigate to **Datacenter → &lt;Node&gt; → &lt;VM&gt;**.
2. Click **Migrate** in the top-right toolbar.
3. Select the **Target node** from the dropdown.
4. Leave **Online** checked (this is the default for running VMs).
5. If the VM uses local storage, check **Force** to enable local disk migration.
6. Click **Migrate** and monitor the task log.

**Via the CLI:**

1. SSH into the source node.
2. Run the migration command:

    ```bash
    qm migrate <vmid> <target-node> --online
    ```

3. If the VM uses local storage, add the `--with-local-disks` flag:

    ```bash
    qm migrate <vmid> <target-node> --online --with-local-disks
    ```

4. Optionally, specify a target storage for the disks:

    ```bash
    qm migrate <vmid> <target-node> --online --with-local-disks --targetstorage <storage-name>
    ```

5. Monitor progress in the task log or terminal output.

!!! warning "When live migration is not possible"
    Live migration will fail if:

    - The VM uses local devices (PCI passthrough, USB passthrough) without `--force`.
    - The target node lacks a network bridge referenced by the VM.
    - The CPU type is set to `host` and the target node has a different CPU model.
    - The VM has snapshots on local storage that cannot be transferred.

---

### 2. Offline-migrate a VM

Offline migration shuts down the VM, copies its disk and configuration to the target node, and optionally restarts it there. Use this when live migration is not possible or when downtime is acceptable.

**Via the web UI:**

1. Shut down the VM from **Datacenter → &lt;Node&gt; → &lt;VM&gt; → Shutdown**.
2. Once the VM is stopped, click **Migrate**.
3. Select the **Target node**.
4. Click **Migrate** and wait for the task to complete.
5. Start the VM on the new node.

**Via the CLI:**

1. SSH into the source node.
2. Shut down the VM:

    ```bash
    qm shutdown <vmid>
    ```

3. Run the offline migration:

    ```bash
    qm migrate <vmid> <target-node>
    ```

4. Optionally, specify a target storage:

    ```bash
    qm migrate <vmid> <target-node> --targetstorage <storage-name>
    ```

5. Start the VM on the target node:

    ```bash
    qm start <vmid>
    ```

!!! tip "When to use offline migration"
    Prefer offline migration when the VM uses PCI/USB passthrough devices, when the source and target nodes have incompatible CPU types with the `host` CPU setting, or when you want to change the storage backend during the move.

---

### 3. Migrate an LXC container

LXC containers in Proxmox do not support true live migration. The closest option is a **restart migration**, which stops the container, moves it, and starts it on the target node. Downtime is typically a few hundred milliseconds to a few seconds.

!!! info "LXC migration restrictions"
    Containers with bind mounts to host paths (e.g., `/mnt/data` on the source node) cannot be migrated unless the same path exists on the target. Containers using device passthrough also cannot be migrated without reconfiguration.

**Restart migration via the web UI:**

1. Navigate to **Datacenter → &lt;Node&gt; → &lt;Container&gt;**.
2. Click **Migrate**.
3. Select the **Target node**.
4. Check **Restart** if the container is running (this enables restart migration).
5. Click **Migrate**.

**Restart migration via the CLI:**

1. SSH into the source node.
2. Migrate a running container with automatic restart:

    ```bash
    pct migrate <ctid> <target-node> --restart
    ```

3. Optionally, remap to a different storage on the target:

    ```bash
    pct migrate <ctid> <target-node> --restart --target-storage <storage-name>
    ```

**Offline migration via the CLI:**

1. Stop the container:

    ```bash
    pct shutdown <ctid>
    ```

2. Migrate the stopped container:

    ```bash
    pct migrate <ctid> <target-node>
    ```

3. Start the container on the target node:

    ```bash
    pct start <ctid>
    ```

---

### 4. Move a disk between storage backends

Storage migration moves a VM or container disk from one storage pool to another without changing the node. This is useful for moving workloads from local storage to shared storage (enabling future live migrations) or for rebalancing disk usage.

**Move a VM disk:**

1. Identify the disk name (e.g., `scsi0`, `ide0`) from the VM's **Hardware** tab or via CLI:

    ```bash
    qm config <vmid>
    ```

2. Move the disk to a new storage:

    ```bash
    qm move-disk <vmid> <disk> <target-storage>
    ```

3. To delete the original copy after the move, add `--delete`:

    ```bash
    qm move-disk <vmid> scsi0 ceph-pool --delete 1
    ```

!!! info "VM can be running"
    You can move a VM disk while the VM is running. Proxmox handles the block-level copy transparently.

**Move a container volume:**

1. Identify the volume name (e.g., `rootfs`, `mp0`) from the container configuration:

    ```bash
    pct config <ctid>
    ```

2. Move the volume to a new storage:

    ```bash
    pct move-volume <ctid> <volume> <target-storage>
    ```

3. For example, to move the root filesystem to shared storage:

    ```bash
    pct move-volume <ctid> rootfs ceph-pool
    ```

!!! warning "Container must be stopped"
    Unlike VM disks, container volumes can only be moved while the container is stopped.

---

### 5. Bulk-migrate all workloads off a node

Before performing maintenance (firmware updates, hardware replacement, RAM upgrades), move all VMs and containers off the node.

1. SSH into the node you want to evacuate.
2. List all VMs on this node:

    ```bash
    qm list
    ```

3. List all containers on this node:

    ```bash
    pct list
    ```

4. Migrate all VMs to a target node using a loop:

    ```bash
    for vmid in $(qm list | awk 'NR>1 {print $1}'); do
      echo "Migrating VM $vmid..."
      qm migrate "$vmid" <target-node> --online --with-local-disks
    done
    ```

5. Migrate all containers to the target node:

    ```bash
    for ctid in $(pct list | awk 'NR>1 {print $1}'); do
      echo "Migrating CT $ctid..."
      pct migrate "$ctid" <target-node> --restart
    done
    ```

6. Verify no workloads remain:

    ```bash
    qm list
    pct list
    ```

!!! tip "Stagger migrations"
    If you have many workloads, run the migrations sequentially (as shown above) rather than in parallel. Concurrent migrations compete for network bandwidth and can cause timeouts.

!!! warning "Check HA configuration"
    If any VMs or containers are managed by the Proxmox HA system, disable HA for them before migrating. Otherwise, HA may try to move them back automatically. Disable HA via **Datacenter → HA → Resources** or with `ha-manager remove <vmid>`.

---

### 6. Troubleshoot common migration errors

**"Bridge 'vmbr1' not found on target node"**

1. Verify bridge names on the target node:

    ```bash
    ssh root@<target-node> "cat /etc/network/interfaces | grep vmbr"
    ```

2. Create the missing bridge on the target node via **&lt;Node&gt; → System → Network → Create → Linux Bridge**, or rename the VM's network interface to match an existing bridge on the target.

**"CPU type 'host' is not compatible with target node"**

1. Change the VM's CPU type to a common baseline before migrating:

    ```bash
    qm set <vmid> --cpu x86-64-v2-AES
    ```

2. Retry the migration.

**"Storage 'local-lvm' is not available on target node"**

1. Either add the same storage name on the target node, or specify a target storage during migration:

    ```bash
    qm migrate <vmid> <target-node> --targetstorage <available-storage>
    ```

**"Migration timed out"**

1. Check network bandwidth between nodes:

    ```bash
    iperf3 -c <target-node-ip>
    ```

2. For large VMs, increase the bandwidth limit or use offline migration.
3. Reduce the VM's dirty-page rate by lowering I/O load inside the VM before retrying.

**"Container has bind mounts -- cannot migrate"**

1. Review the container configuration for bind mounts:

    ```bash
    pct config <ctid> | grep mp
    ```

2. Remove or replace bind mounts with volume mounts before migrating.

---



## Revision History

| Date       | Version | Changes                | Author | Contributors |
|------------|---------|------------------------|--------|--------------|
| 2026-04-09 | 1.0     | Initial guide creation | Jaime Motjé    |              |
