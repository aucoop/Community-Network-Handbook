# I have more than one site. What are my options?

So it can happen that your community (or company or whatever, remember that since we did that with the comunity network principle in mind we focus on that, but this could really be the case for a company) is geographically scattered across different sites. Instead of speaking in general terms, we will take again the Hahatay Network as an example.

Remember in previous section we had the Sunukeur site. We said the Sunukeur site's ISP router was located in Mamadou's house. But that's not true. In reallity the ISP is in another site: the Fess building.

We essentially have two problems to solve here: the physical problem and the network design problem. Let's focus first in the physical problem.

## The Physical Connection

Networks needs some physical support, and this is either through air or through a cable. Cable gets automatically discarded since the distance between sunukeur and fess is more than 2km, and also Hahatay does not own the land in between. We only have air left.

Through the air we are limited only to certain technologies that are use unlicensed bands. Just to not get in too many detail, there are some frequency bands were you can emit as much as you want without any restriction (well there are power restrictions, but that's it), .e.g, wifi (there are others such as LoRa) and there are other frequency that you cannot emit, such as FM frequency (that's why radio stations need to ask for permission to emit, let's say in 93.9).

So yes, at your home you (what we did in section 2.1.1 you can have wifi because essentially you are emiting in an unlicensed band. Some countries such as the US for example have some unlicensed bands in 4G as well. But wifi is unlicensed worldwide.

So coming back to our problem again. We have to connect our sites through air, 2km. So a cheap and reliable solution is to use radio links.

Radio links are essentially point to pint wifi links that are specially designed for a use case like this.

TODO diagram / photo

Since this is an opinionated guide, we strongly recommend ubiquiti radio links. We are not in any way affiliated with them, but they turned out to be sell really good devices at a very good prices and those are relatively easy to get worldwide (for example we can easily buy them in Senegal).

The first step to connect your sites is to check ubiquiti's tool. It's a very nice tool they provide where you basically tell them your two sites, place them in a map and they will recommend you which product should you buy for your use case.

Second step we call it the "visibility test". Just try to put some visible object in one site, then go to the other site and try to see it with your eyes, prismaticos or whatever. If you manage to have direct visibility site-to-site. You are very good to go. For example in the rural Senegal this is fairly easy since there are no big buildings nor big trees and everything is pretty flat.
