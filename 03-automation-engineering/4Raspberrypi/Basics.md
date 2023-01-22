
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



# SSH
---

A common error that I encounter every time i change the ip address but keep the hostname same.
(basically, everytime I fresh start on with ip I name it batpi but the static ip keeps changing.)

The specific error is as shown here 
![image](../_assets/ssh-error.png)

Refer [How To Fix the "Warning: Remote Host Identification Has Changed" Error (kinsta.com)](https://kinsta.com/knowledgebase/warning-remote-host-identification-has-changed/), In short clear the txt in known_hosts file present in C:\\Users\\some-name\\.ssh\\


