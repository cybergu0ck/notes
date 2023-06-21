

## Introduction to cloud computing
---

Cloud computing is the delivery of computing services over the internet.

Computing services include common IT infrastructure such as

-   virtual machines
-   storage
-   databases
-   networking

Cloud services also expand the traditional IT offerings to include things like

-   Internet of Things (IoT)
-   machine learning (ML)
-   artificial intelligence (AI)



Introductory Video:

[What is cloud computing - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/3-what-cloud-compute)



> Microsoft Azure is a cloud computing platform with an ever-expanding set of services to help you build solutions to meet your business goals.

<br/>

## The shared responsibility model
---

With the shared responsibility model, these responsibilities of maintaining the physical space, ensuring security, and maintaining or replacing the servers get shared between the cloud provider and the consumer.

Physical security, power, cooling, and network connectivity are the responsibility of the cloud provider.

At the same time, the consumer is responsible for the data and information stored in the cloud.

Then, for some things, the responsibility depends on the situation. If you’re using a cloud SQL database, the cloud provider would be responsible for maintaining the actual database. However, you’re still responsible for the data that gets ingested into the database. If you deployed a virtual machine and installed an SQL database on it, you’d be responsible for database patches and updates, as well as maintaining the data and information stored in the database.

1.  IaaS places the most responsibility on the consumer, with the cloud provider being responsible for the basics of physical security, power, and connectivity.
2.  On the other end of the spectrum, SaaS places most of the responsibility with the cloud provider.
3.  PaaS, being a middle ground between IaaS and SaaS, rests somewhere in the middle and evenly distributes responsibility between the cloud provider and the consumer.



![[Pasted image 20221210142802.png]]

<br/>

## The Cloud Models
---

The cloud models define the deployment type of cloud resources. The three main cloud models are:

1.  private
2.  public
3.  Hybrid

### Private cloud

A private cloud is, in some ways, the natural evolution from a corporate datacenter. It’s a cloud (delivering IT services over the internet) that’s used by a single entity.

Private cloud provides much greater control for the company and its IT department. However, it also comes with greater cost and fewer of the benefits of a public cloud deployment.

Finally, a private cloud may be hosted from your onsite datacenter. It may also be hosted in a dedicated datacenter offsite, potentially even by a third party that has dedicated that datacenter to your company.

### Public cloud

A public cloud is built, controlled, and maintained by a third-party cloud provider. With a public cloud, anyone that wants to purchase cloud services can access and use resources. The general public availability is a key difference between public and private clouds.

### Hybrid clo0ud

A hybrid cloud is a computing environment that uses both public and private clouds in an inter-connected environment.

A hybrid cloud environment can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources. Hybrid cloud can be used to provide an extra layer of security.

For example, users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure.


## Consumption Based Models
---

When comparing IT infrastructure models, there are two types of expenses to consider.

1.  Capital expenditure (CapEx) :

CapEx is typically a one-time, up-front expenditure to purchase or secure tangible resources. A new building, repaving the parking lot, building a datacenter, or buying a company vehicle are examples of CapEx.

1.  operational expenditure (OpEx) :

OpEx is spending money on services or products over time. Renting a convention center, leasing a company vehicle, or signing up for cloud services are all examples of OpEx.

Cloud computing falls under OpEx because cloud computing operates on a consumption-based model.

-   With cloud computing, you don’t pay for the physical infrastructure, the electricity, the security, or anything else associated with maintaining a datacenter. Instead, you pay for the IT resources you use. If you don’t use any IT resources this month, you don’t pay for any IT resources.

This consumption-based model has many benefits, including:

-   No upfront costs.
-   No need to purchase and manage costly infrastructure that users might not use to its fullest potential.
-   The ability to pay for more resources when they're needed.
-   The ability to stop paying for resources that are no longer needed.

To put it another way, cloud computing is a way to rent compute power and storage from someone else’s datacenter.



[[2. Describe the benefits of using cloud services]]