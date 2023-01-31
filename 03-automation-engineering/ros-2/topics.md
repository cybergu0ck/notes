Topics are a vital element of the ROS graph that act as a bus for nodes to exchange messages, Topics are one of the main ways in which data is moved between nodes and therefore between different parts of the system.

> A node may publish data to any number of topics and simultaneously have subscriptions to any number of topics.

<br/>

# checking list of topics 

- checking list of topics
	```bash
	ros2 topic list
	```
	
	When we run the above code after running `ros2 run turtlesim turtlesim_node` and `ros2 run turtlesim turtle_teleop_key`, we get:
	```
	/parameter_events
	/rosout
	/turtle1/cmd_vel
	/turtle1/color_sensor
	/turtle1/pose
	```

- checking list of topics along with their topic types
	```bash
	ros2 topic list -t
	```
	what we get is 
	```
	/parameter_events [rcl_interfaces/msg/ParameterEvent]
	/rosout [rcl_interfaces/msg/Log]
	/turtle1/cmd_vel [geometry_msgs/msg/Twist]
	/turtle1/color_sensor [turtlesim/msg/Color]
	/turtle1/pose [turtlesim/msg/Pose]
	``` 

> These attributes, particularly the type, are how nodes know they’re talking about the same information as it moves over topics.

<br/>

# To see what is being published on a topic

```bash
ros2 topic echo <topic_name>
```

In our case, If we run the below command and then move the turtle using the teleop terminal we'll get subsequent results
```
ros2 topic echo /turtle1/cmd_vel
```

```
linear:
  x: 2.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
  ---
```

<br/>

# Getting topic info

```bash
ros2 topic info <topic name>
```

```bash
ros2 topic info /turtle1/cmd_vel
```

This will return,
```
Type: geometry_msgs/msg/Twist
Publisher count: 1
Subscription count: 2
```

<br/>

# Interface show


```bash
ros2 interface show <msg tyoe>
```

- Nodes send data over topics using messages. Publishers and subscribers must send and receive the same type of message to communicate.

- The topic types we saw earlier after running `ros2 topic list -t` let us know what message type is used on each topic. Recall that the `cmd_vel` topic has the type:  `geometry_msgs/msg/Twist`

- This means that in the package `geometry_msgs` there is a `msg` called `Twist`

To get the interface, particularly to get the structure of the data the message expects, we run
```bash
ros2 interface show geometrymsgs/msg/Twist
```
For the message type from above it yields:,
```
This expresses velocity in free space broken into its linear and angular parts.

    Vector3  linear
            float64 x
            float64 y
            float64 z
    Vector3  angular
            float64 x
            float64 y
            float64 z
```

This tells you that the `/turtlesim` node is expecting a message with two vectors, `linear` and `angular`, of three elements each. If you recall the data we saw `/teleop_turtle` passing to `/turtlesim` with the `echo` command, it’s in the same structure. [[topics#To see what is being published on a topic]]

<br/>

# Publishing to a topic directly

```bash
ros2 topic pub <topic_name> <msg_type> '<args>'
```

- The `'<args>'` argument is the actual data you’ll pass to the topic, in the structure you just discovered in the previous section.
- It’s important to note that this argument needs to be input in YAML syntax.

```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
Note that args something like x:2.0 will give error, it must be x: 2.0 (space in between)

- Here `--once` is an optional argument meaning “publish one message then exit”.
- To steadily operate the robot, we can use `--rate 1` for 1 Hz


<br/>
<br/>

# The gist

```bash
ros2 topic list
ros2 topic list -t
ros2 topic echo <topic_name>
ros2 topic info <topic name>
ros2 interface show <msg type>
ros2 topic pub --once <topic name> <msg type> <args>
```