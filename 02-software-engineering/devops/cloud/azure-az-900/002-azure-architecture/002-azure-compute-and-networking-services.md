

You’ll learn about three of the compute options (virtual machines, containers, and Azure functions). You’ll also learn about some of the networking features, such as Azure virtual networks, Azure DNS, and Azure ExpressRoute.

-   VMs provide infrastructure as a service (IaaS) in the form of a virtualized server and can be used in many ways. Just like a physical computer, you can customize all of the software running on your VM.

-   However, as an IaaS offering, you still need to configure, update, and maintain the software that runs on the VM.

-   VMs are an ideal choice when you need:

-   Total control over the operating system (OS).
-   The ability to run custom software.
-   To use custom hosting configurations.

-   An image is a template used to create a VM and may already include an OS and other software, like development tools or web hosting environments.
-   You can create and provision a VM in minutes when you select a preconfigured VM image.



# Scale VMs in Azure

 VMs can be grouped together to provide high availability, scalability, and redundancy. Azure can also manage the grouping of VMs for you with features such as scale sets and availability sets.

## Virtual machine scale sets

-   Virtual machine scale sets let you create and manage a group of identical, load-balanced VMs.

-   If you simply created multiple VMs with the same purpose, you’d need to ensure they were all configured identically and then set up network routing parameters to ensure efficiency. You’d also have to monitor the utilization to determine if you need to increase or decrease the number of VMs. With Azure's Virtual machine scale sets, these tasks are automated.

## Virtual machine availability sets

Availability sets are designed to ensure that VMs stagger updates and have varied power and network connectivity, preventing you from losing all your VMs with a single network or power failure.

Availability sets do this by grouping VMs in two ways: update domain and fault domain.

1.  Update domain: The update domain groups VMs that can be rebooted at the same time. This allows you to apply updates while knowing that only one update domain grouping will be offline at a time. All of the machines in one update domain will be updated. An update group going through the update process is given a 30-minute time to recover before maintenance on the next update domain starts.

1.  Fault domain: The fault domain groups your VMs by common power source and network switch. By default, an availability set will split your VMs across up to three fault domains. This helps protect against a physical power or networking failure by having VMs in different fault domains (thus being connected to different power and networking resources).

## Examples of when to use VMs

Some common examples or use cases for virtual machines include:

-   During testing and development. VMs provide a quick and easy way to create different OS and application configurations. Test and development personnel can then easily delete the VMs when they no longer need them.
-   When running applications in the cloud. The ability to run certain applications in the public cloud as opposed to creating a traditional infrastructure to run them can provide substantial economic benefits. For example, an application might need to handle fluctuations in demand. Shutting down VMs when you don't need them or quickly starting them up to meet a sudden increase in demand means you pay only for the resources you use.
-   When extending your datacenter to the cloud: An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and adding VMs to that virtual network. Applications like SharePoint can then run on an Azure VM instead of running locally. This arrangement makes it easier or less expensive to deploy than in an on-premises environment.
-   During disaster recovery: As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can get significant cost savings by using an IaaS-based approach to disaster recovery. If a primary datacenter fails, you can create VMs running on Azure to run your critical applications and then shut them down when the primary datacenter becomes operational again.

## Move to the cloud with VMs (Lift and Shift)

VMs are also an excellent choice when you move from a physical server to the cloud

## VM Resources

When you provision a VM, you’ll also have the chance to pick the resources that are associated with that VM, including:

-   Size (purpose, number of processor cores, and amount of RAM)
-   Storage disks (hard disk drives, solid state drives, etc.)
-   Networking (virtual network, public IP address, and port configuration)




# Create an Azure Virtual Machine

You could use the Azure portal, the Azure CLI, Azure PowerShell, or an Azure Resource Manager (ARM) template. In this instance, azure cli is used

1.  From Cloud Shell, run the following az vm create command to create a Linux VM:

`az vm create \`

  `--resource-group learn-a54d2f79-2885-4369-abe2-c4a02e981006 \`

  `--name my-vm \`

  `--image UbuntuLTS \`

  `--admin-username azureuser \`

  `--generate-ssh-keys`

1.  Run the following az vm extension set command to configure Nginx on your VM:

`az vm extension set \`

  `--resource-group learn-a54d2f79-2885-4369-abe2-c4a02e981006 \`

  `--vm-name my-vm \`

  `--name customScript \`

  `--publisher Microsoft.Azure.Extensions \`

  `--version 2.1 \`

  `--settings '{"fileUris":["https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"]}' \`

  `--protected-settings '{"commandToExecute": "./configure-nginx.sh






# Azure Virtual Desktop

Another type of virtual machine is the Azure Virtual Desktop. Azure Virtual Desktop is a desktop and application virtualization service that runs on the cloud. It enables you to use a cloud-hosted version of Windows from any location.

Check out this video [https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/4-virtual-desktop](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/4-virtual-desktop) to get it's overview.




# Azure Containers

## What are containers?

-   Containers are a virtualization environment.
-   Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host. Unlike virtual machines, you don't manage the operating system for a container.
-    Containers are lightweight and designed to be created, scaled out, and stopped dynamically.
-   Containers are designed to allow you to respond to changes on demand. With containers, you can quickly restart if there's a crash or hardware interruption. One of the most popular container engines is Docker, which is supported by Azure.

The following video highlights several of the important differences between virtual machines and containers:

[https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers)

## Azure Container Instances

Azure Container Instances offer the fastest and simplest way to run a container in Azure; without having to manage any virtual machines or adopt any additional services. Azure Container Instances are a platform as a service (PaaS) offering. Azure Container Instances allow you to upload your containers and then the service will run the containers for you.



# Azure Functions

-   Azure Functions is an event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers.
-   If you build an app using VMs or containers, those resources have to be “running” in order for your app to function. With Azure Functions, an event wakes the function, alleviating the need to keep resources provisioned when there are no events.

## Benefits of Azure Functions

-   Using Azure Functions is ideal when you're only concerned about the code running your service and not about the underlying platform or infrastructure. Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service, and when that work can be completed quickly, within seconds or less.

-   Functions scale automatically based on demand, so they may be a good choice when demand is variable.

-   Azure Functions runs your code when it's triggered and automatically deallocates resources when the function is finished. In this model, you're only charged for the CPU time used while your function runs.

-   Functions can be either stateless or stateful. When they're stateless (the default), they behave as if they're restarted every time they respond to an event. When they're stateful (called Durable Functions), a context is passed through the function to track prior activity.

-   Functions are a key component of serverless computing. ([https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions))

# Application hosting options

-   VMs give you maximum control of the hosting environment and allow you to configure it exactly how you want. VMs also may be the most familiar hosting method if you’re new to the cloud.

-   Containers, with the ability to isolate and individually manage different aspects of the hosting solution, can also be a robust and compelling option.

-   There are other hosting options that you can use with Azure, including Azure App Service.

Azure App Service is a robust hosting option that you can use to host your apps in Azure. Azure App Service lets you focus on building and maintaining your app, and Azure focuses on keeping the environment up and running. Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It supports multiple languages, including .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. It also supports both Windows and Linux environments.



# Azure Virtual Networking

Azure virtual networks and virtual subnets enable Azure resources, such as VMs, web apps, and databases, to communicate with each other, with users on the internet, and with your on-premises client computers.

Azure virtual networks provide the following key networking capabilities:

-   Isolation and segmentation
-   Internet communications
-   Communicate between Azure resources
-   Communicate with on-premises resources
-   Route network traffic
-   Filter network traffic
-   Connect virtual networks

Azure virtual networking supports both public and private endpoints to enable communication between external or internal resources with other internal resources.

-   Public endpoints have a public IP address and can be accessed from anywhere in the world.
-   Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network.

## Isolation and segmentation

Azure virtual network allows you to create multiple isolated virtual networks.

When you set up a virtual network, you define a private IP address space by using either public or private IP address ranges. The IP range only exists within the virtual network and isn't internet routable. You can divide that IP address space into subnets and allocate part of the defined address space to each named subnet. For name resolution, you can use the name resolution service that's built into Azure. You also can configure the virtual network to use either an internal or an external DNS server.

## Internet communications

You can enable incoming connections from the internet by assigning a public IP address to an Azure resource, or putting the resource behind a public load balancer.

## Communicate between Azure resources

You'll want to enable Azure resources to communicate securely with each other. You can do that in one of two ways:

-   Virtual networks can connect not only VMs but other Azure resources, such as the App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual machine scale sets.
-   Service endpoints can connect to other Azure resource types, such as Azure SQL databases and storage accounts. This approach enables you to link multiple Azure resources to virtual networks to improve security and provide optimal routing between resources.

## Communicate with on-premises resources

 In effect, you can create a network that spans both your local and cloud environments. There are three mechanisms for you to achieve this connectivity:

1.  Point-to-site virtual private network connections are from a computer outside your organization back into your corporate network. In this case, the client computer initiates an encrypted VPN connection to connect to the Azure virtual network.
2.  Site-to-site virtual private networks link your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network. In effect, the devices in Azure can appear as being on the local network. The connection is encrypted and works over the internet.
3.  Azure ExpressRoute provides a dedicated private connectivity to Azure that doesn't travel over the internet. ExpressRoute is useful for environments where you need greater bandwidth and even higher levels of security.

## Route network traffic

By default, Azure routes traffic between subnets on any connected virtual networks, on-premises networks, and the internet. You also can control routing and override those settings, as follows:

-   Route tables allow you to define rules about how traffic should be directed. You can create custom route tables that control how packets are routed between subnets.
-   Border Gateway Protocol (BGP) works with Azure VPN gateways, Azure Route Server, or Azure ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

## Filter network traffic

Azure virtual networks enable you to filter traffic between subnets by using the following approaches:

-   Network security groups are Azure resources that can contain multiple inbound and outbound security rules. You can define these rules to allow or block traffic, based on factors such as source and destination IP address, port, and protocol.
-   Network virtual appliances are specialized VMs that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing wide area network (WAN) optimization.

## Connect virtual networks

You can link virtual networks together by using virtual network peering. Peering allows two virtual networks to connect directly to each other. Network traffic between peered networks is private, and travels on the Microsoft backbone network, never entering the public internet. Peering enables resources in each virtual network to communicate with each other. These virtual networks can be in separate regions, which allows you to create a global interconnected network through Azure.

User-defined routes (UDR) allow you to control the routing tables between subnets within a virtual network or between virtual networks. This allows for greater control over network traffic flow.



# Azure Virtual Private Networks

A virtual private network (VPN) uses an encrypted tunnel within another network. VPNs are typically deployed to connect two or more trusted private networks to one another over an untrusted network (typically the public internet). Traffic is encrypted while traveling over the untrusted network to prevent eavesdropping or other attacks. VPNs can enable networks to safely and securely share sensitive information.

## VPN gateways

A VPN gateway is a type of virtual network gateway. Azure VPN Gateway instances are deployed in a dedicated subnet of the virtual network and enable the following connectivity:

-   Connect on-premises datacenters to virtual networks through a site-to-site connection.
-   Connect individual devices to virtual networks through a point-to-site connection.
-   Connect virtual networks to other virtual networks through a network-to-network connection.

When you deploy a VPN gateway, you specify the VPN type: either policy-based or route-based. The main difference between these two types of VPNs is how traffic to be encrypted is specified. In Azure, both types of VPN gateways use a pre-shared key as the only method of authentication.

1.  Policy-based VPN gateways specify statically the IP address of packets that should be encrypted through each tunnel. This type of device evaluates every data packet against those sets of IP addresses to choose the tunnel where that packet is going to be sent through.
2.  In Route-based gateways, IPSec tunnels are modeled as a network interface or virtual tunnel interface. IP routing (either static routes or dynamic routing protocols) decides which one of these tunnel interfaces to use when sending each packet. Route-based VPNs are the preferred connection method for on-premises devices. They're more resilient to topology changes such as the creation of new subnets.

### High-availability scenarios

If you’re configuring a VPN to keep your information safe, you also want to be sure that it’s a highly available and fault tolerant VPN configuration. There are a few ways to maximize the resiliency of your VPN gateway.

### Active/standby

By default, VPN gateways are deployed as two instances in an active/standby configuration, even if you only see one VPN gateway resource in Azure. When planned maintenance or unplanned disruption affects the active instance, the standby instance automatically assumes responsibility for connections without any user intervention. Connections are interrupted during this failover, but they're typically restored within a few seconds for planned maintenance and within 90 seconds for unplanned disruptions.

### Active/active

In this configuration, you assign a unique public IP address to each instance. You then create separate tunnels from the on-premises device to each IP address. You can extend the high availability by deploying an additional VPN device on-premises.

### ExpressRoute failover

Another high-availability option is to configure a VPN gateway as a secure failover path for ExpressRoute connections. ExpressRoute circuits have resiliency built in. However, they aren't immune to physical problems that affect the cables delivering connectivity or outages that affect the complete ExpressRoute location.

### Zone-redundant gateways

In regions that support availability zones, VPN gateways and ExpressRoute gateways can be deployed in a zone-redundant configuration. This configuration brings resiliency, scalability, and higher availability to virtual network gateways.




# Azure ExpressRoute

Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider. This connection is called an ExpressRoute Circuit. With ExpressRoute, you can establish connections to Microsoft cloud services, such as Microsoft Azure and Microsoft 365. This allows you to connect offices, datacenters, or other facilities to the Microsoft cloud. Each location would have its own ExpressRoute circuit.

ExpressRoute connections don't go over the public Internet. This allows ExpressRoute connections to offer more reliability, faster speeds, consistent latencies, and higher security than typical connections over the Internet.

There's lot more about it, checkout [https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/11-expressroute](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/11-expressroute)





# Azure DNS

Azure DNS is a hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure.

## Benefits of Azure DNS

Azure DNS leverages the scope and scale of Microsoft Azure to provide numerous benefits, including:

-   Reliability and performance
-   Security
-   Ease of Use
-   Customizable virtual networks
-   Alias records