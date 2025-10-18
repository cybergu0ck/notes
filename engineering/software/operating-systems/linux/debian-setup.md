# Setting up Debian machine

<br>
<br>
<br>

## Add current user to sudoers file

1. Become super user

   ```
   su -
   ```

1. Edit sudoers file, find the line `root ALL=(ALL:ALL) ALL` and add current user the same way under it.

   ```
   visudo
   ```

<br>
<br>
<br>

## Usage of external monitor

Follow this to close the laptop lid and only use the external monitor as main display.

* Identify the identifier of external monitor (example: HDMI-1-1) and update the following sh file.

    ```sh
    #!/bin/bash

    # The script will automatically use secondary monitor and turn off the primary laptop monitor if secondary monitor is connected
    # Modify the following script with correct names for displays.
    # Determine the name of the displays (ex eDP-1, HDMI-1-1 etc) using `xrandr` command.


    if xrandr | grep "HDMI-1-1 connected"; then
        echo "HDMI-1-1 is connected. Switching display to HDMI-1-1 and turning off eDP-1."
        xrandr --output eDP-1 --off --output HDMI-1-1 --auto
    else
        echo "HDMI-1-1 is not connected. Enabling eDP-1."
        xrandr --output eDP-1 --auto 
    fi
    ```

* Give execute permissions for the sh file.

    ```
    sudo chmod +x /path/to/your/script.sh
    ```

* If display manager is used, which generally kicks in before the the desktop environment, configure the display manager to use  the external monitor if it is hooked.

    * If lightdm display manager is used, then add the script path to the  `display-setup-script=` variable in lightdm.conf file in "/etc/lightdm/"

        ```
        sudo nano /etc/lightdm/lightdm.conf
        ```
* Configure the desktop environemtn to use the external monitor.

    * If i3 is used as desktop environment, the config is updated to run the above script on i3 startup.
    * The following changes are needed for other desktop environments (better to use the following even with i3). Modify the line `HandleLidSwitch=` to `ignore` in the following file.

        ```
        sudo nano /etc/systemd/logind.conf
        ```

<br>
<br>
<br>

## Configure git

1. Install git

   ```
   sudo apt install git
   ```

1. Set the username and email

   ```
   git config --global user.name <username>
   ```

   ```
   git config --global user.email <email>
   ```

<br>
<br>

### Setup SSH keys

- Generate a new SSH key. Follow [docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
- Add the new key to github. Follow [docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

<br>
<br>
<br>

## Install vscode

Follow [official docs](https://code.visualstudio.com/docs/setup/linux)


<br>
<br>
<br>


## Install programs

1. Install i3 (tiling window manager) for desktop environment.

   ```
   sudo apt install i3
   ```

1. Install rofi for dmenu feature.

   ```
   sudo apt install rofi
   ```

1. Install pulseaudio for volume control.

   ```
   sudo apt install pavucontrol
   ```

1. Install flameshot for screenshot utitlity. The key binding of `$mod+Shift+s` is set in i3 config.

   ```
   sudo apt install flameshot
   ```

1. Install blueman for bluetooth manager.

   ```
   sudo apt install blueman
   ```

1. Install vlc for media player.

   ```
   sudo apt install vlc
   ```

<br>
<br>
<br>

## Stow the dotfiles


1. Install stow

   ```
   sudo apt install stow
   ```

1. Clone the dotfiles repo in "/home/user" directory.

1. cd into dotfiles directory and use stow command

   ```
   stow .
   ```

<br>
<br>
<br>

## Configure lightdm

* Follow [docs](https://wiki.debian.org/LightDM) to configure lightdm.

* To enable the user list,

    ```
    [Seat:*]
    greeter-hide-users=false
    ```
