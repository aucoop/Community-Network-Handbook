# Network Planning

This guide walks you through assessing a location for network deployment—whether starting from scratch or expanding an existing setup.

This guide implements the concepts introduced in
[Chapter 2.1 — The First Router](../../2-Imaginary-Use-Case/2.1-The-First-Router/index.md) and
[Chapter 2.2 — Expanding Coverage](../../2-Imaginary-Use-Case/2.2-Expanding-Coverage/index.md).

## What You'll Learn

- How to evaluate whether internet connectivity exists at your site
- Tools and techniques for surveying Wi-Fi coverage and identifying dead zones
- Methods for measuring baseline internet speed
- How to map your site and plan access point placement
- Decision criteria for choosing expansion technologies

## Prerequisites

- A smartphone or laptop with Wi-Fi capability
- Access to the physical site you want to assess
- Basic understanding of Wi-Fi signal strength concepts

---

## Overview

The following flowchart shows the complete network planning process from initial assessment to technology selection:

```mermaid
flowchart TD
    subgraph Phase1["Phase 1: Internet Assessment"]
        START([Arrive at Site]) --> CHECK{Internet<br/>connection<br/>exists?}
        CHECK -->|No| RESEARCH[Research available ISPs<br/>Fiber, Cable, ADSL, 4G/5G, Satellite]
        RESEARCH --> BUDGET[Create budget comparison<br/>Cost, Speed, Data caps]
        BUDGET --> USAGE[Define expected usage<br/>Users, devices, applications]
        USAGE --> SELECT[Select ISP with community]
        SELECT --> INSTALL[Install internet service]
        INSTALL --> ENTRY[Internet connection ready]
        
        CHECK -->|Yes| IDENTIFY[Identify current technology]
        IDENTIFY --> EVALUATE{Current speed <br/>meets usage needs?}
        EVALUATE -->|No| CHANGEABLE{Can change<br/>provider?}
        CHANGEABLE -->|Yes| BUDGET
        CHANGEABLE -->|No| DOCUMENT[Document alternatives<br/>for future reference]
        DOCUMENT --> ENTRY
        EVALUATE -->|Yes| ENTRY
    end
    
    subgraph Phase2["Phase 2: Site Assessment"]
        ENTRY --> SURVEY[Survey Wi-Fi coverage<br/>with analyzer app]
        SURVEY --> DEADZONES[Identify dead zones<br/>and weak areas]
        DEADZONES --> SPEEDTEST[Measure baseline<br/>internet speed]
        SPEEDTEST --> MAP[Map physical site<br/>buildings, obstacles, power]
    end
    
    subgraph Phase3["Phase 3: Expansion Planning"]
        MAP --> PLAN[Plan access point<br/>placement]
        PLAN --> TECH{Choose expansion<br/>technology}
        TECH --> SAME{Same<br/>building?}
        SAME -->|Yes| ETHERNET[Ethernet + Access Points]
        SAME -->|No| CABLE{Can run<br/>cables?}
        CABLE -->|Yes| ETHERNET
        CABLE -->|No| DISTANCE{Distance<br/>< 50m?}
        DISTANCE -->|Yes| MESH[Mesh Wi-Fi]
        DISTANCE -->|No| PTP[Point-to-Point Wifi Antennas]
        
        ETHERNET --> DEPLOY([Deploy Network])
        MESH --> DEPLOY
        PTP --> DEPLOY
    end
```

Each phase is covered in detail in its own section:

1. [Internet Assessment](1-Internet-Assessment.md) — Evaluate your internet connection or find one
2. [Site Assessment](2-Site-Assessment.md) — Survey coverage, measure speed, and map the site
3. [Expansion Planning](3-Expansion-Planning.md) — Place access points and choose technologies

---

## Revision History

| Date       | Version | Changes                | Author           | Contributors |
|------------|---------|------------------------|------------------|--------------|
| 2026-04-05 | 1.0     | Initial guide creation | Maria Jover        |              |
