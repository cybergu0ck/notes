
## Finding the current IP address
---

```shell
hostname -I
```


## Find the routers gateway IP address
---
```shell
ip r | grep default
```


Find the DNS IP address
---
```shell
sudo nano /etc/resolv.conf
```


## Enabling static IP address
---
Edit the dhcpcd.conf file

```shell
sudo nano /etc/dhcpcd.conf
```

```
# dhcpcd.conf

interface <strong>NETWORK</strong>  
static ip_address=<strong>STATIC_IP</strong>/24  
static routers=<strong>ROUTER_IP</strong>  
static domain_name_servers=<strong>DNS_IP</strong>
```

	NETWORK : eth0 or wlan0
	STATIC_IP : desired static IP address
	ROUTER_IP : the gateway IP address
	DNS_IP : the DNS IP address