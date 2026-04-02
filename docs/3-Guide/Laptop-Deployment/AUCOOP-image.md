# AUCOOP Linux Deployment Image

The **AUCOOP Linux Mint image** is a customized system image designed for mass deployment to refurbished laptops. This page explains the design decisions behind the AUCOOP image and provides principles for creating your own tailored deployment image.

This image is used as the "golden master" in [Phase 1 of the Laptop Deployment guide](index.md#phase-1----prepare-the-golden-master).

---

## Why Linux Mint?

After analyzing different operating systems, Linux Mint emerged as the most suitable choice for community center deployments:

### System Comparison

| Feature                     | Windows | Ubuntu  | Linux Mint |
|-----------------------------|---------|---------|------------|
| Open Source                | No      | Yes     | Yes        |
| Lightweight for older PCs  | No      | Moderate| Yes        |
| UI similarity to Windows   | Yes     | No      | Yes        |
| Productivity tools (Office)| Commercial | Open Source | Open Source |
| License cost               | Per machine | Free | Free      |

**Why not Windows?**

- Licensing fees make it expensive for batch deployments
- Reduced performance on older hardware
- Requires activation and regular license validation

**Why not Ubuntu?**

- GNOME desktop is unfamiliar to Windows users
- Requires more user training for basic navigation

**Why Linux Mint?**

- Cinnamon desktop environment closely mimics the Windows experience
- Optimized performance for older hardware
- Familiar Start menu, taskbar, and system tray layout
- Free and open source

!!! info "Work in Progress"
    **Suggested image:** Screenshot comparing Windows 11, Ubuntu GNOME, and Linux Mint Cinnamon desktops side-by-side to illustrate UI similarity.

---

## AUCOOP Customizations

To make the image ready for community use with minimal training, the AUCOOP team implemented these enhancements:

### 1. OnlyOffice Suite

Replaced LibreOffice with OnlyOffice, which more closely mimics Microsoft Office in interface and file compatibility.

```bash
# On the golden master machine:
sudo apt remove --purge libreoffice-*
sudo apt install onlyoffice-desktopeditors
```

!!! info "Work in Progress"
    **Suggested image:** Side-by-side comparison of Microsoft Word and OnlyOffice Document Editor showing interface similarity.

### 2. Custom Desktop Launchers

Created desktop shortcuts with familiar names and icons:

- **Word** → OnlyOffice Document Editor
- **Excel** → OnlyOffice Spreadsheet Editor
- **PowerPoint** → OnlyOffice Presentation Editor

This reduces cognitive friction — users click what they recognize.

!!! info "Work in Progress"
    **Suggested image:** Screenshot of the AUCOOP desktop showing the custom launchers with Word/Excel/PowerPoint-style icons.

### 3. System Simplification

Removed pre-installed applications that add complexity without value for this use case:

```bash
sudo apt remove --purge thunderbird pidgin transmission-gtk hexchat
sudo apt autoremove -y
```

### 4. Standard User Account

Created a single shared user account (`aucoop`) with a known password. All deployed machines boot directly to this account, ready to use.

### 5. Network and Hostname

- Set a generic hostname (`aucoop-desktop`) — this will be the same on all machines
- Pre-configured network settings for automatic DHCP

---

## Principles for Creating Similar Images

When creating your own deployment image, follow these guidelines:

### 1. Design for Your Users' Existing Knowledge

If your users are familiar with Windows, choose an interface that resembles it. If they already use LibreOffice, keep it. **Meet users where they are** rather than forcing new patterns.

### 2. Remove Unnecessary Complexity

Every application, menu item, and configuration option increases the support burden. **Start minimal** and add tools only when requested.

### 3. Test on Representative Hardware

Install and test the golden master on hardware that matches your target machines (same age, same specs). If the oldest machine runs smoothly, all others will too.

### 4. Document Customizations

Keep a text file or script listing every package installed, removed, or configured. This makes it possible to:

- Recreate the image months later
- Troubleshoot issues
- Explain what's different from stock Linux Mint

### 5. Version Your Images

Use descriptive image names like `aucoop-mint22.3-2026-03` that include:

- The base OS and version
- The date created
- Optionally, a revision number if you iterate

---

## Creating Your Golden Master

To create your own customized image:

1. **Install the base OS** on one reference machine (e.g., Linux Mint 22.3 Cinnamon)
2. **Apply customizations** (install/remove packages, configure desktop, create user accounts)
3. **Clean up temporary files** (see [Step 1 in the deployment guide](index.md#1-set-up-the-reference-machine))
4. **Capture the image** with Clonezilla (see [Phase 2](index.md#phase-2----capture-the-image-with-clonezilla))

The golden master is then stored as a Clonezilla disk image and deployed via PXE boot to all target machines.

!!! info "Work in Progress"
    **Suggested image:** Photo of a "golden master" laptop with a sticky note label, showing the concept of the reference machine.

---

## References

- Linux Mint Project -- <https://linuxmint.com/>
- OnlyOffice Desktop Editors -- <https://www.onlyoffice.com/desktop.aspx>
- Labdoo Project -- <https://www.labdoo.org/> (refurbished laptops for education)
