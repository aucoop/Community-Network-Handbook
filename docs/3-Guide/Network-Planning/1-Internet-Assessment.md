# Internet Assessment

Before you can plan a network, you need internet. This section helps you evaluate what you have — or find what's available.

This guide implements the concept introduced in
[Chapter 2.1 — The First Router](../../2-Imaginary-Use-Case/2.1-The-First-Router/index.md).

---

## Determine your starting point

When you arrive at a site, you face one of two scenarios: either there is an existing internet connection, or there is none.

### If there is no internet connection

1. Research internet service providers (ISPs) available in the area. Common options include:
    - Fiber
    - Cable Broadband
    - ADSL
    - 4G/5G Mobile Router
    - Low Earth Orbit Satellites (e.g., Starlink)

2. Check the country's ISP websites for available plans and coverage maps.

3. For satellite coverage, check [Starlink's availability map](https://starlink.com/map).

4. Speak with local contacts to understand what connectivity options are commonly used in the area.

5. Create a budget comparison using the template below. Download and complete it for each ISP option:

    [:material-download: Download ISP Budget Comparison Template (CSV)](downloads/isp-budget-comparison.csv){ .md-button }

    The template guides you through three steps:

    1. **Define your usage profile** — Document expected users, primary applications, peak hours, and minimum requirements
    2. **Compare ISP offerings** — Fill in each provider's specifications side by side
    3. **Calculate weighted scores** — Rate each ISP against your requirements and calculate a total score

    | Criterion | Weight | Why it matters |
    |-----------|--------|----------------|
    | Meets download speed needs | 5 | Core functionality depends on this |
    | Within budget | 5 | Sustainability requires affordability |
    | No restrictive data cap | 4 | Unexpected overage fees disrupt operations |
    | Reliability reputation | 4 | Downtime affects all network users |
    | Meets upload speed needs | 3 | Important for video calls and file sharing |
    | Acceptable latency | 3 | Critical for real-time applications |
    | Local support available | 3 | Faster problem resolution |
    | No long-term contract | 2 | Flexibility to change if needs evolve |

    !!! tip "Match the plan to the use case"
        Different network uses have vastly different bandwidth requirements. Before selecting a plan, define how many users will connect simultaneously, what applications they will use (web browsing, video streaming, file transfers), and during which hours peak usage will occur. This understanding drives the right choice.

6. Discuss the options with the community and select the most appropriate ISP.

### If there is an existing internet connection

1. Identify the current technology in use (Fiber, Cable, ADSL, 4G/5G, Satellite).

2. Perform the budget comparison exercise above to verify the current solution is optimal.

    !!! info "Working with constraints"
        Sometimes the internet service is provided by a government entity or institution and cannot be changed. Even so, document the alternatives for future reference.

3. Locate the internet entry point—this is where your network planning begins.

---

## References

- [Starlink Coverage Map](https://starlink.com/map)
