# Docker Command Line Deployment

- Run this in terminal

  ```
  docker run -d --name jellyfin \
          --user 1000:1000 \
          -p 8096:8096 \
          -p 8920:8920  \
          --volume /home/bat/containers/jellyfin/config:/config \
          --volume /home/bat/containers/jellyfin/cache:/cache  \
          --mount type=bind,source=/home/bat/containers/jellyfin/media,target=/media \
          --restart=unless-stopped \
          jellyfin/jellyfin
  ```

- If the above one fails, then run this one liner

  ```
  docker run -d --name jellyfin --user 1000:1000 -p 8096:8096 -p 8920:8920  --volume /home/bat/containers/jellyfin/config:/config --volume /home/bat/containers/jellyfin/cache:/cache  --mount type=bind,source=/home/bat/containers/jellyfin/media,target=/media --restart=unless-stopped jellyfin/jellyfin
  ```
