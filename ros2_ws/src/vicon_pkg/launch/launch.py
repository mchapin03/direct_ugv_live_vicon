from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='vicon_pkg',
            executable='vicon_node',
            name='vicon_publisher',
            output='screen',
            parameters=[
                {'config': 'config.cfg'}
            ]
        )
    ])