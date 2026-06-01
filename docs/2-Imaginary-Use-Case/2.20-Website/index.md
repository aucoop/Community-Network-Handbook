# *"Let's show the world what we built!"*

You've built something remarkable: a fully functional community network with local services, monitoring, backups, user management, and a public domain pointing at it. You know how much work went into it. The problem is that nobody *else* does. The funder who might support the next phase, the volunteer who'd love to help, the community across the valley wondering if they could do the same — none of them can see any of it. The network is real and invisible at the same time.

A **website** is how you make it visible. It's the front door to the project: the place where the story of what you built, why, and for whom finally becomes something you can point people to.

## Why it's worth the effort

A website is more than a brochure — for a community network it does real, load-bearing work:

- **It documents the project.** What the network is, who it serves, how it works. This both helps the community understand what they own and helps other communities learn from what you did.
- **It attracts support.** Funding, volunteers, partnerships, and donated hardware tend to flow toward projects that are visible and credible. A clear website is often the first thing a potential supporter looks for — and its absence is a quiet "no."
- **It inspires replication.** A big part of the point of community networks is that others copy them. A website that tells your story is how the model spreads to the next village.
- **It demonstrates accountability.** Donors and supporters want to see impact. A site with updates, photos, and outcomes shows their support went somewhere real — and makes the *next* ask far easier.

## Host it outside your network

This is the one service whose whole job is to be reachable from the outside world — which is exactly why it should **not** live on your own network. A community network's uplink is often the most constrained and least reliable part of the whole system. If the website rides on it, then the moment your link or local hardware goes down, the project becomes invisible at precisely the time a funder or partner might be looking. Worse, every visitor from the public internet is then pulling traffic back through your scarce upstream bandwidth.

The good news: hosting a project site externally is free and easy, because it should be a **static site** — a generator like **Hugo** or **MkDocs** (the same tool that builds *this handbook*) turns simple text files into a fast, secure site with no database and nothing to patch urgently.

A few practical choices to make:

- **Publish on free static hosting.** **GitHub Pages**, GitLab Pages, Cloudflare Pages, or Netlify will host a static site for free, on fast infrastructure built to be reachable, with HTTPS handled for you. Point your domain at it and you're done. If you need something with a server you control, a cheap **VPS** is the next step up — but still off your own network.
- **Static over dynamic.** For a project site, a static generator is the right default: nothing to hack, nothing to patch urgently, trivially cheap to run, and fast for visitors anywhere. Reach for a heavier CMS only if non-technical people genuinely need to edit content through a web interface.
- **Write for outsiders.** The audience isn't you; it's people who've never heard of the project. Lead with what it is and why it matters, show photos of the real thing, and make it obvious how to get in touch or get involved.

This is the project stepping into the open — turning everything you've built behind the scenes into a story the world can find, learn from, and support.

!!! tip "Guide reference"
    For website setup and hosting instructions, see [Guide — Website](../../3-Guide/Website/index.md).
