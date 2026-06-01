# Case study template

A Chapter 4 entry is a write-up of a community network that has actually been deployed. The goal is to give a future reader enough information to understand the design choices, learn from what worked and didn't, and ideally replicate the parts that fit their context.

## How to start

1. Copy the existing [Namibia case study](../4-Real-Use-Cases/4.1-Namibia/index.md) (`docs/4-Real-Use-Cases/4.1-Namibia/index.md`) as your template.
2. Create a new folder under `docs/4-Real-Use-Cases/` — for example `4.2-YourLocation/`.
3. Drop your `index.md` and an `images/` subfolder inside.
4. Adapt the structure to your deployment. Keep section headings consistent with existing case studies so readers know where to look for what.
5. Add an entry under `4. Real Use Cases` in `mkdocs.yml`.
6. Open a pull request.

## What to cover

Every case study should answer these four questions:

- **Context.** Where is the network? Who is it for? What problems existed before — no connection at all, unreliable connection, no internal network, no shared services?
- **Design.** What technologies did you choose, and why? Where did you depart from this handbook's defaults, and what motivated the change?
- **Deployment.** What was the on-the-ground experience? What worked smoothly? What broke, and how did you recover? What would you do differently next time?
- **Current state.** Is the network still running? How has it evolved since the first deployment? Who is operating it today?

## Images

- Co-located `images/` subfolder inside the case-study folder.
- `.webp` format.
- Before/after network diagrams are very valuable if you have them — see how the Namibia case uses `4.1-network-before.webp` and `4.1-network-after.webp`.
- Maps of the site can help readers picture the physical context.

## Honesty over polish

A case study is more useful when it includes what didn't go well. The next team to deploy in similar conditions will run into the same problems — your write-up is what lets them avoid the same week of debugging.
