# Docker Installation on Raspberry Pi OS Lite

1. Update and Upgarde packages

   ```
   sudo apt update && sudo apt upgrade
   ```

2. Install docker using script (we are trusting docker here)

   ```
   curl -sSL https://get.docker.com | sh
   ```

3. Add our users to docker group

   ```
   sudo usermod -aG docker $USER
   ```

4. logout for the changes to take effect

   ```
   logout
   ```

5. Verify wether `docker` group is present in groups

   ```
   groups
   ```

6. Test Docker

   ```
   docker run hello-world
   ```
