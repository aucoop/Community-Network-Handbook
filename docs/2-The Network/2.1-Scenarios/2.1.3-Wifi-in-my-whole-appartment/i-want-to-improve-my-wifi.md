# I want wifi in my appartment

Now, having wifi connectivyt in the same room where you have your ISP's router is tipically not enough, even for a city appartment. That's quite common in appartments in the city.

One simple way to improve wifi signal is by simply adding wifi repeaters. Is what the OpenWrt community call a "Dumb AP".

For that you tipically want a router that is not really powerful. We don't care that much about its CPU / microchip or RAM memory, we want good radio technology, e.g.Wifi 5,6. You have our recommendations for this kind of routers in Section 2.2.3.

## Setting up a Dumb AP

OpenWrt guide is pretty decent, although we could write here owr own version of it.

## Considerations with Dumb AP

Adding to many Dumb APs is not recommendable, but again, sometimes enough is good enough. The cost of setting up Dumb APs is really low. You can get really cheap and good routers to be Dumb APs. So our recommendation is that you go and try it.

According to X,Y,Z having more than N APs in the same network makes wifi work really bad. I have not really never deployed more than one AP, but I don't have really explored the limits of this approach.

If you want a more sophisticated approach to extend the wifi network, you can try to go with this two:

* Mesh Networks (802.11s staandard (There are others, but probably you don't need more than that at this point.))
* Fast Roaming (802.11r standard)

If you are reading this from Europe or the United States and have studied in a university, you probably have connected to a network called "eduroam". So "eduroam" is basically a very big wifi network that works across university. It has some fancy authentication stuff where you can basically authenticate with the ID of your university (let's say in UPC in Barcelona) and then go to another university (let's say Universidad de Granada) and with my credentials for the UPC I can connect to Universidad de Granada automatically.

But we do not care much about the auth stuff. In this very big "eduroam" network you can move across the university campus and you will always have good wifi signal, no matter where you go. This is most likely fast roaming, and basically your laptop or phone connected to the wifi always sees "eduroam" network, but in reality the network is "smart" enough to change the AP you are connected with at every time.
