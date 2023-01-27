
# Create a user account
---
```sh
sudo adduser <username>
```


# Delete a user account
---
```sh
sudo deluser --remove-home <username>
```


# Add a user to `sudo` group
---
```sh
sudo adduser <username> sudo
```

# Install and Enable ssh
---
```sh
sudo apt update
sudo apt install openssh-server
```

```sh
sudo systemctl status ssh
```

```sh
sudo ufw allow ssh
```

