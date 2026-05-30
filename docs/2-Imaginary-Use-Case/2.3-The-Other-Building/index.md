# *"What about the building across the street?"*

The main building is fully covered. Every classroom, the office, even the courtyard — all online. But the moment you look beyond the walls, the problem changes shape entirely. The library across the street. The workshop 500 meters down the road. The clinic at the far edge of the village. Regular WiFi, the kind that struggles to cross a concrete wall, has no hope of bridging those distances.

You can't run a cable, either — not across a public street, not across someone else's land, not for half a kilometer through terrain that floods. And paying for a separate internet connection at every building defeats the whole point: you already *have* internet at the main building. You just need to carry it to the others.

The answer is a **point-to-point wireless link** — a dedicated radio connection between two fixed locations using directional antennas. Where an ordinary router sprays signal in every direction (and so reaches no single place very far), a point-to-point link concentrates all its energy into a tight beam aimed from one rooftop straight at another. Think of it as an invisible cable strung through the air: it behaves like a wire between the two buildings, carrying your network from the site that has internet to the site that needs it.

This is the technique that turns a single connected building into a connected *community*. Get one good uplink, and you can relay it building by building across surprising distances — as long as the antennas can see each other.

## Can WiFi really go that far?

Yes — with the right equipment. Regular WiFi routers use omnidirectional antennas that spread signal in all directions, which is great for filling a room and useless for reaching across a valley. Point-to-point links flip that logic: they use **directional antennas** that focus all their energy into a narrow beam, trading wide coverage for raw reach. The same radio power that fades to nothing after 30 meters in every direction can hold a solid link over kilometers when it's all pointed one way.

Products like Ubiquiti's airMAX or LiteBeam are designed exactly for this. They operate on unlicensed frequencies (5 GHz) and can link buildings **kilometers apart** — with clear line of sight, far more than most communities will ever need.

## Plan the link before you buy

The single biggest predictor of success is **line of sight**. Radio at these frequencies travels in a straight line and does not forgive obstacles. Trees, buildings, hills — even the curvature of the earth over long distances — sit between your two antennas and quietly kill the link. Before spending a cent, you want to know whether A and B can actually "see" each other, and how high you'd need to mount the antennas to clear what's in the way.

We strongly recommend using the [Ubiquiti Antenna Simulator (ispdesign)](https://ispdesign.ui.com/) to plan your links. You drop a pin on point A and point B, tell it the bandwidth you'd like, and it does the hard math for you: it accounts for distance, terrain, altitudes, and even the earth's curvature, then recommends a specific antenna model and mounting height that will satisfy your requirements.

!!! tip "Play with it!"
    We strongly recommend spending a few minutes playing with this simulator before you commit to any hardware. Put in the two points you want to connect and the bandwidth you'd like; it will take the orography, the altitudes, and even the earth's curvature into account, then hand you a concrete antenna model sized for your site. It turns "I hope this works" into "I know this works."

## Rules of thumb for radio links

The simulator does the calculations, but a few field realities are worth internalizing:

- **Line of sight is everything.** The antennas must truly see each other. A single tree that grows into the path, or a new building, can take the link down. Plan for the path to stay clear.
- **Height wins.** Mounting antennas on rooftops or poles dramatically improves the link by lifting the beam over obstacles. In practice, getting antennas high and solidly mounted is usually the most time- and resource-consuming part of the whole job — budget for it.
- **Alignment matters.** The beam is narrow. A few degrees off and your strong link becomes a flaky one or disappears entirely. Aim carefully and lock the mount down so wind can't nudge it.
- **A link is only as good as its weakest end.** Both antennas must be sized and aimed correctly; a perfect dish on one rooftop pointed at a poorly mounted one on the other still gives you a poor link.

## A note on Ubiquiti

!!! info "We're not affiliated"
    We are in no way affiliated with the brand. They don't provide open-source software and they aren't 100% aligned with our principles on how networks should be built. But this is a **100% opinionated guide**, and we believe Ubiquiti provides genuinely good hardware and software at a very reasonable price. As one data point: we have €60 antennas that have run 24/7 for six years under the African sun in Senegal, and they're still going. For point-to-point links, **Ubiquiti earns its place here** — use the simulator and buy their gear with confidence.

!!! tip "Guide reference"
    For detailed antenna setup and alignment instructions, see [Guide — Antennas](../../3-Guide/Antennas/index.md).
