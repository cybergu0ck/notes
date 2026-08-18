# Linux Shell

The **shell** is a program that takes keyboard commands and passes them to the operating system to carry out.

- _sh_ is the original Unix shell program written by Steve Bourne.
- _bash_ is the enhanced version of sh (bash for bourne again shell) and all distros supply bash from the GNU project.

<br/>
<br/>
<br/>

## Terminal Emulators

- When using a graphical user interface, Terminal emulators give us access to the shell.

  - KDE uses "konsole"
  - GNOME uses "gnome-terminal", though it’s likely called simply “terminal” on our menu

- Shell Prompt : starts with `username@machinename`, followed by the current working directory and a dollar sign.

- If the last character of the prompt is a hash mark (#) rather than a dollar sign ($), the terminal session has superuser privileges which means that either we are logged in as the root user or we’ve selected a terminal emulator that provides superuser (administrative) privileges.

<br/>
<br/>
<br/>

## About mouse and focus

A mechanism built into the X Window System (the underlying engine that makes the GUI go) supports a quick copy-and-paste technique.

- If you highlight some text by holding down the left mouse button and
  dragging the mouse over it (or double-clicking a word), it is copied into a buffer maintained by X. Pressing the middle mouse button will cause the text to be pasted at the cursor location.

- Don’t be tempted to use CTRL-C and CTRL-V to perform copy and paste
  inside a terminal window. They don’t work.

<br>
<br>
<br>
