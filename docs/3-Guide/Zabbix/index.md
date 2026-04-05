# Zabbix — Monitoring and Alerts

Know when something breaks before your users do. Zabbix is an open-source, enterprise-grade monitoring platform built around a central server that collects data from lightweight agents and SNMP-enabled devices. It gives you real-time visibility into every router, server, and antenna in your network, fires alerts when things go wrong, and keeps historical data so you can spot trends and plan ahead.

This section implements the concepts introduced in
[Chapter 2 — Monitoring](../../2-Imaginary-Use-Case/2.5-Monitoring/index.md).

## What You'll Learn

- Understanding the Zabbix architecture (server, agent, SNMP)
- Installing Zabbix server on a Proxmox LXC container or bare metal
- Adding hosts to Zabbix: OpenWrt routers (Zabbix Agent), antennas (SNMP), and Docker servers (Zabbix Agent 2)
- Configuring alert triggers (device down, high CPU, disk full)
- Setting up Telegram bot notifications for real-time alerts on problems and recoveries
- Creating useful dashboards for network-wide visibility

!!! info "Work in Progress"
    Alert trigger configuration and dashboard setup guides are not yet written.

## Guides

- [Install Zabbix Server on Proxmox](Install-Zabbix.md) — deploy a Zabbix server container using the community helper scripts
- [Add Hosts to Zabbix](Add-Hosts.md) — register OpenWrt routers, antennas, and Docker servers as monitored hosts
- [Set Up Telegram Notifications](Telegram-Notifications.md) — receive instant Telegram alerts when something goes wrong
