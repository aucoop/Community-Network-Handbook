# *"We have 20 laptops and no time to set them up one by one"*

Someone donated a batch of refurbished laptops to the community center. They need an operating system, a standard user account, and the right software for the classrooms. Great news — until you realize you have to set up each one manually. Install the OS, create the user, configure the desktop, install packages... times twenty.

That's a full week of mind-numbing repetition. And if you make a mistake on laptop number fifteen, you have to start over.

**There's a better way.** You prepare one laptop exactly how you want it — the **golden master** — and then clone that image to every other machine over the network. All twenty laptops boot from the network, receive the image, and reboot into a ready-to-use system. The whole process takes less than half a day.

The technique is called **PXE network boot** (Preboot Execution Environment). You set up a server on a local switch that acts as a DHCP server, a file server, and an image server. The laptops boot from the network instead of their hard drive, receive a cloning tool called **Clonezilla**, and Clonezilla writes the golden master image to their disk.

This is the same approach used by IT departments to deploy hundreds of machines — adapted here for a community network with off-the-shelf hardware and free software.

### Customizing Your Image

The day the computers reached the community center, the excitement was palpable. New tools, new horizons! But with each laptop powered on, reality stepped in: how do we prepare them for the people waiting outside of the computer lab?

Not just any system would do. The team decides to sit down and mapp out what the community truly needed and different ideas came up: Clutter-free so as not to overwhelm new users. Intuitive tools echoing what people already know. No surprises; no installations gone rogue. Web browsers to connect worlds... 

By focusing on **simplicity, optimization**, and **usability**, what started as intimidating blank slates became the promise of transformation now that the community knows what will suit its purpuse we can replicate it for all the new aquired computers!

!!! tip "Guide reference"
    For step-by-step setup of the networking deployment process and image creation methodology, continue to [Guide -- Laptop Deployment](../../3-Guide/Laptop-Deployment/index.md).

---

**Next steps:**

- [How do I actually set up the PXE server and deploy?](../../3-Guide/Laptop-Deployment/index.md)
