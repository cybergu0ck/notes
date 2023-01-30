

# Running executables using `ros2 run`

```bash
ros2 run <package_name> <executable_name>
```

Example, running the ***executable*** `turtlesim_node` from the ***package*** `turtlesim` :
```bash
ros2 run turtlesim turtlesim_node
```

<br/>
<br/>


# Nodes

A node is a fundamental ROS 2 element that serves a single, modular purpose in a robotics system.

<br/>


## List all nodes using `ros2 node list`

```bash
ros2 node list
```

If we run the above command (after runnin the above executable, i.e. the Node must be active), we get the name of the node as "/turtlesim"
```bash
/turtlesim
```


<br/>

## Remapping

```bash
ros2 run <package_name> <excutable> --ros-args --remap __node:= <new_node_name>
```

For example, remaping 
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```

And now if we run `ros2 node list`, we see
```
/my_turtle
```

However, this is not permanent meaning if we run `ros2 run turtlesim turtlesim_node` again, we can see that the node name is back to '/turtlesim' and not '/my_turtler'.

<br/>

## Getting info of the node

```bash
ros2 node info <node_name>
```


Note that the node must be active (running) and the node name must prefix with / in the command (Or i guess the node name always starts with /)
```
ros2 node info /turtlesim
```

The above command will output,

```
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /my_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /my_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /my_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /my_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /my_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /my_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```