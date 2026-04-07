from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Path to your nav2_params.yaml
    nav2_params_file = os.path.join(
        os.getcwd(), 'src/ugv_nav/config/nav2_params.yaml'
    )

    # Include the standard Nav2 bringup launch file
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                os.getenv('NAV2_BRIINGUP', '/opt/ros/humble/share/nav2_bringup/launch'),
                'navigation_launch.py'
            )
        ),
        launch_arguments={
            'params_file': nav2_params_file
        }.items()
    )

    # Directly remap /cmd_vel
    return LaunchDescription([
        nav2_launch,
        Node(
            package='ugv_nav',
            executable='nav2_bringup', 
            name='nav2_remapped',
            remappings=[('/cmd_vel', '/diffbot_base_controller/cmd_vel_unstamped')],
            parameters=[{'params_file': nav2_params_file}]
        )
    ])