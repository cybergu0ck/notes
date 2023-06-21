# Deployment

1. Create the config file in desired directory and download a sample conf.yml

   ```
   sudo wget -qO /opt/dashy/config/conf.yml https://raw.githubusercontent.com/Lissy93/dashy/master/public/conf.yml
   ```

2. Run the docker command

   ```
   docker run -d \
   -p 8080:80 \
   -v /custom/path/conf.yml:/app/public/conf.yml \
   --name dashboard \
   --restart=always \
   lissy93/dashy:arm64v8
   ```

- For more info [Refer Here](https://lindevs.com/install-dashy-inside-docker-container-in-linux)
