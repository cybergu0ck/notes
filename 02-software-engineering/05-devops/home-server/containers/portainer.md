# Deployment

- Run the following as is

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

- See this video to solve [DB Tech](https://www.youtube.com/watch?v=q6PimerKycI&ab_channel=DBTech)
