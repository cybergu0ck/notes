# Installation

- Run the following

```
docker run -d \
  -p 9443:9443 \
  --name portainer \
  --restart unless-stopped \
  -v data:/data \
  -v /var/run/docker.sock:/var/run/docker.sock \
  portainer/portainer-ce:latest
```

<br>
<br>

# Issues

## Published Ports not working issue

See this video to solve [DB Tech](https://www.youtube.com/watch?v=q6PimerKycI&ab_channel=DBTech)

sudo docker run -d -p 9000:9000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest --logo "https://www.flaticon.com/free-icon/bat-black-silhouette-with-opened-wings_30208?term=bat&page=1&position=33&origin=search&related_id=30208" || error "Failed to run Portainer docker image!"
