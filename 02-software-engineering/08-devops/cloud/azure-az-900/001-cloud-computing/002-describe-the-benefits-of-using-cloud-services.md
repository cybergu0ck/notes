

When building or deploying a cloud application, two of the biggest considerations are uptime (or availability) and the ability to handle demand (or scale).

## High availability

 High availability focuses on ensuring maximum availability, regardless of disruptions or events that may occur.

When you’re architecting your solution, you’ll need to account for service availability guarantees. Azure is a highly available cloud environment with uptime guarantees depending on the service. These guarantees are part of the service-level agreements (SLAs).

Watch this video to understand about SLAs:

[https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud)

## Scalability

Another major benefit of cloud computing is the scalability of cloud resources. Scalability refers to the ability to adjust resources to meet demand.

Scaling generally comes in two varieties: vertical and horizontal.

-   Vertical scaling is focused on increasing or decreasing the capabilities of resources.
-   Horizontal scaling is adding or subtracting the number of resources.

1.  Vertical scaling

With vertical scaling, if you were developing an app and you needed more processing power, you could vertically scale up to add more CPUs or RAM to the virtual machine. Conversely, if you realized you had over-specified the needs, you could vertically scale down by lowering the CPU or RAM specifications.

1.  Horizontal scaling

With horizontal scaling, if you suddenly experienced a steep jump in demand, your deployed resources could be scaled out (either automatically or manually). For example, you could add additional virtual machines or containers, scaling out. In the same manner, if there was a significant drop in demand, deployed resources could be scaled in (either automatically or manually), scaling in.

## Reliability

Reliability is the ability of a system to recover from failures and continue to function.

With a decentralized design, the cloud enables you to have resources deployed in regions around the world. With this global scale, even if one region has a catastrophic event other regions are still up and running. You can design your applications to automatically take advantage of this increased reliability. In some cases, your cloud environment itself will automatically shift to a different region for you, with no action needed on your part.

## Predictability

Predictability can be focused on performance predictability or cost predictability.

1.  Performance : Performance predictability focuses on predicting the resources needed to deliver a positive experience for your customers.

-    Autoscaling, load balancing, and high availability are just some of the cloud concepts that support performance predictability.

1.  Cost : Cost predictability is focused on predicting or forecasting the cost of the cloud spend.

-   By operating in the cloud and using cloud analytics and information, you can predict future costs and adjust your resources as needed. You can even use tools like the Total Cost of Ownership (TCO) or Pricing Calculator to get an estimate of potential cloud spend.

## Governance

Whether you’re deploying infrastructure as a service or software as a service, cloud features support governance and compliance. Things like set templates help ensure that all your deployed resources meet corporate standards and government regulatory requirements.

## Security

If you want maximum control of security, infrastructure as a service provides you with physical resources but lets you manage the operating systems and installed software, including patches and maintenance. If you want patches and maintenance taken care of automatically, platform as a service or software as a service deployments may be the best cloud strategies for you.

## Management of the cloud

Management of the cloud speaks to managing your cloud resources. In the cloud, you can:

-   Automatically scale resource deployment based on need.
-   Deploy resources based on a preconfigured template, removing the need for manual configuration.
-   Monitor the health of resources and automatically replace failing resources.
-   Receive automatic alerts based on configured metrics, so you’re aware of performance in real time.

## Management in the cloud

Management in the cloud speaks to how you’re able to manage your cloud environment and resources. You can manage these:

-   Through a web portal.
-   Using a command line interface.
-   Using APIs.
-   Using PowerShell.


[[3. Cloud Service Types]]