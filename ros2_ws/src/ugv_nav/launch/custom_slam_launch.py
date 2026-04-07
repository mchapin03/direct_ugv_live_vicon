from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import LogInfo

def generate_launch_description():
    return LaunchDescription([
        # Optional: You can log a message that the launch has started
        LogInfo(
            condition=None,
            msg="Starting SLAM Toolbox with Debug Logging!"
        ),
        Node(
            package='slam_toolbox',
            executable='slam_toolbox_node',
            name='slam_toolbox',
            parameters=[{'params-file': 'params-file:=~/ros_ws/src/ugv_nav/config/mapper_params_online_async.yaml'}],
            output='screen',
            log_level='debug',  # Set the log level to debug
        ),
    ])