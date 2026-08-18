# Introduction

<br>
<br>
<br>

## Workspaces

“Workspace” is a ROS term for the location on your system where you’re developing with ROS 2.

- The core ROS 2 workspace is called the underlay.
- Subsequent local workspaces are called overlays.

<br>
<br>

### Sourcing

- Combining workspaces makes developing against different versions of ROS 2, or against different sets of packages, easier.
- This is accomplished by sourcing setup files every time you open a new shell, or by adding the source command to your shell startup script once.
- Without sourcing the setup files, it is unable to access ROS 2 commands, or find or use ROS 2 packages.

<br>

```sh
source /opt/ros/jazzy/setup.bash
```

<br>
<br>
<br>

## Executables

<br>
<br>

### Print the list of executables

- To see the list of executables of a package.

  ```bash
  ros2 pkg executables <packagename>
  ```

  ```bash
  >ros2 pkg executables turtlesim
  turtlesim draw_square
  turtlesim mimic
  turtlesim turtle_teleop_key
  turtlesim turtlesim_node
  ```

<br>
<br>

### Running executables

```bash
ros2 run <package_name> <executable_name>
```

<br>
<br>
<br>

## Turlesim

Turtlesim is a lightweight simulator for learning ROS 2.

- Install the package

  ```bash
  sudo apt update
  sudo apt install ros-jazzy-turtlesim
  ```

- Start the turtlesim.

  ```bash
  ros2 run turtlesim turtlesim_node
  ```

- Use the turtlesim

  ```bash
  ros2 run turtlesim turtle_teleop_key
  ```
