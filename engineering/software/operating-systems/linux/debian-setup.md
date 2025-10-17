# Setting up Debian

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

## Add a new SSH key

- Generate a new SSH key. Follow [docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
- Add the new key to github. Follow [docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

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

## Set laptop lid close behaviour

```
sudo nano /etc/systemd/logind.conf
```

Modify the line `HandleLidSwitch=` to `ignore`.

<br>
<br>

## Configure i3wm

1. Install i3

   ```
   sudo apt install i3
   ```

1. Install stow

   ```
   sudo apt install stow
   ```

1. Install rofi

   ```
   sudo apt install rofi
   ```

1. Clone the dotfile repo.

1. cd into dotfiles directory and use stow command

   ```
   stow .
   ```

<br>
<br>

## Install utilities

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

## Install vscode

Follow [official docs](https://code.visualstudio.com/docs/setup/linux)