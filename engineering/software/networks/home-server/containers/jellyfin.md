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
  
  
- Try this 

  ```
  docker run -d \
    --name=jellyfin \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Etc/UTC \
    -e JELLYFIN_PublishedServerUrl=192.168.0.5 `#optional` \
    -p 8096:8096 \
    -p 8920:8920 `#optional` \
    -p 7359:7359/udp `#optional` \
    -p 1900:1900/udp `#optional` \
    -v /path/to/library:/config \
    -v /path/to/tvseries:/data/tvshows \
    -v /path/to/movies:/data/movies \
    --restart unless-stopped \
    lscr.io/linuxserver/jellyfin:latest
  ```

- If the above one fails, then run this one liner

  ```
  docker run -d --name jellyfin --user 1000:1000 -p 8096:8096 -p 8920:8920  --volume /home/bat/containers/jellyfin/config:/config --volume /home/bat/containers/jellyfin/cache:/cache  --mount type=bind,source=/home/bat/containers/jellyfin/media,target=/media --restart=unless-stopped jellyfin/jellyfin
  ```
