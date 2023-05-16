# Installing samba on linux

- Follow this [ubuntu tutorial](https://ubuntu.com/tutorials/install-and-configure-samba#4-setting-up-user-accounts-and-connecting-to-share)

1. Install samba

   ```
   sudo apt update
   sudo apt install samba
   ```

2. Make a directory for the share

   ```
   mkdir /home/{user}/samba-share
   ```

3. Edit the smb.conf file

   ```
   sudo nano /etc/samba/smb.conf
   ```

- At the bottom of the file, add the following lines:

  ```
  [sambashare]
      comment = Samba on Ubuntu
      path = /home/username/sambashare
      read only = no
      browsable = yes
  ```

4. Set up samba user accounts

   ```
   sudo smbpasswd -a {username}
   ```

5. Access in windows by using `\\ip-adress`
