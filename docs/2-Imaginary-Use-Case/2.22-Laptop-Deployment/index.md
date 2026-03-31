# *"We have 20 laptops and no time to set them up one by one"*

Someone donated a batch of refurbished laptops to the community center. They need an operating system, a standard user account, and the right software for the classrooms. Great news — until you realize you have to set up each one manually. Install the OS, create the user, configure the desktop, install packages... times twenty.

That's a full week of mind-numbing repetition. And if you make a mistake on laptop number fifteen, you have to start over.

**There's a better way.** You prepare one laptop exactly how you want it — the **golden master** — and then clone that image to every other machine over the network. All twenty laptops boot from the network, receive the image, and reboot into a ready-to-use system. The whole process takes less than half a day.

The technique is called **PXE network boot** (Preboot Execution Environment). You set up a server on a local switch that acts as a DHCP server, a file server, and an image server. The laptops boot from the network instead of their hard drive, receive a cloning tool called **Clonezilla**, and Clonezilla writes the golden master image to their disk.

This is the same approach used by IT departments to deploy hundreds of machines — adapted here for a community network with off-the-shelf hardware and free software.

### Customizing Your Image

To ensure the laptops are ready for their end users, one option is to create your own customized Linux image. By doing so, the system can be tailored to meet specific needs. Some key principles to consider when creating your image include:

- **Less is more:** Focus on simplicity and eliminate unnecessary software to facilitate adoption.
- **Optimized for older hardware:** A lightweight system ensures good performance across all laptops.
- **Familiar interface:** Use an intuitive, user-friendly desktop environment to minimize the learning curve.
- **Pre-installed Applications:** Include only essential tools like office suites and web browsers that align with the users' needs.

By following these principles, you can create a solution that is both functional and accessible, enabling the devices to serve the community effectively.

!!! tip "Guide reference"
    For step-by-step setup of the networking deployment process and image creation methodology, continue to [Guide -- Laptop Deployment](../../3-Guide/Laptop-Deployment/index.md).

---

**Next steps:**

- [How do I actually set up the PXE server and deploy?](../../3-Guide/Laptop-Deployment/index.md)
