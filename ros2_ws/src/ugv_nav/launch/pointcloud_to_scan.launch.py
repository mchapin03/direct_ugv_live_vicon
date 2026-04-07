from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            name='pointcloud_to_laserscan',
            parameters=[{
                'target_frame': 'base_link',
                'min_height': 0.0,
                'max_height': 1.0,
                'range_min': 0.1,
                'range_max': 10.0,
            }],
            remappings=[
                ('cloud_in', '/camera/camera/depth/color/points'),
                ('scan', '/scan'),
            ]
        )
    ])