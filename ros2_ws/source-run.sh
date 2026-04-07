#!/bin/bash

colcon build
# Source your ROS 2 workspace
source ~/ros2_ws/install/setup.bash
echo "sourced"
# Launch the dumbot bringup
ros2 launch dumbot_bringup minimal.launch.py
