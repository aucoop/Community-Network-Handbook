# Zabbix -- Monitoring and Alerts

Know when something breaks before your users do.

This section implements the concepts introduced in
[Chapter 2 -- Monitoring](../../2-Imaginary-Use-Case/2.5-Monitoring/index.md).

## What You'll Learn

- Adding hosts to Zabbix: OpenWrt routers (Zabbix Agent), antennas (SNMP), and Docker servers (Zabbix Agent 2)
- Setting up Telegram bot notifications for real-time alerts on problems and recoveries
- Installing Zabbix server (on Proxmox or bare metal)
- Configuring alert triggers (down, high CPU, disk full)
- Creating useful dashboards

!!! info "Work in Progress"
    The Zabbix server installation guide, alert trigger configuration, and dashboard setup are not yet written.

<!-- TODO: Installation steps, alert trigger configuration, dashboard creation guide -->

## Guides

- [Add Hosts to Zabbix](Add-Hosts.md) -- register OpenWrt routers, antennas, and Docker servers as monitored hosts
- [Set Up Telegram Notifications](Telegram-Notifications.md) -- receive instant Telegram alerts when something goes wrong
