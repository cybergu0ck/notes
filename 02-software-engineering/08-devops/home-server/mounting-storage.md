# Find the Disk Identifier

- Find the disk using any of the following commands, it will something like /dev/sde1
  ```
  lsblk
  ```
  ```
  sudo fdisk -l
  ```

<br>
<br>
<br>

# Check for partion

- Use something like `/dev/sde1` for disk identifier
  ```
  sudo gdisk <disk identifier>
  ```

<br>
<br>
<br>

# Create GPT partition

- GPT is the ideal partition, so stick to it

* To create a new GPT partition, follow this :

  1. Start with the following command.

  ```
  sudo gdisk <disk identifier>
  ```

  1. When it asks for Command, type `n` for new partition
  1. Set Partition Number as 1
  1. Confirm the rest of the enteries (leave it blank)
  1. When it asks for Command, type `w` to write and confirm it
  1. GPT partition has been created

<br>
<br>
<br>

# Make a ext4 File System

- ext4 is the ideal file system, so stick to it
- THIS WILL WIPE THE DRIVE!

  ```
  sudo mkfs.ext4 <disk identifier>
  ```

* Wait while it says Creating Journal (...blocks) and while it is Writing superblocks and filesystem accounting information!

<br>
<br>
<br>

# Check the filesystem (can get UUID of disk)

- Use the following command, the file system will be referred as TYPE, so TYPE = "ext4" means ext4 filesystem.

* We can get the UUID of the disk using this command too.

  ```
  sudo blkid
  ```

<br>
<br>
<br>

# Making mount persistant (mount on boot)

- We must use fstab present in etc.

1. Open the fstab file

   ```
   sudo nano /etc/fstab
   ```

2. Enter the follwing in it

   ```
   UUID=<uuid of disk without quotes> <location of mount> <file system> defaults 0 0
   ```

   - Example:
     ```
     UUID=3adds386b-e1ae-4032-ai33-0c50f5ecc4ac /mnt/drive ext4 defaults 0 0
     ```
   - UUID can be got using `sudo blkid`.
   - If we donot want linux to check the disk on boot we keep the last two digits as 0 0.
   - If we want linux to check the disk on boot and if the disk contains the OS to boot we must specify last two digits as 0 1.
   - If we want linux to check the disk on boot and if the disk doesnt contain os, we must specify last two digits as 0 2.

- Make sure the path contains the directories mentioned for mount
- Mount the disk using the followin command

<br>
<br>
<br>

# Moutning the disk

- Use this command to mount the disk

  ```
  sudo mount -a
  ```

<br>
<br>
<br>

# Unmounting a disk

* It is not "unmount" but it is "umount"

  ```
  sudo unmount <disk identifier>
  ```
