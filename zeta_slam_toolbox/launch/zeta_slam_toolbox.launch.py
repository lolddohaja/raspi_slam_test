from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_share_directory = get_package_share_directory('zeta_slam_toolbox')
    parameter_file = LaunchConfiguration('zeta_slam_toolbox_params', default=PathJoinSubstitution([package_share_directory, 'params', 'zeta_slam_toolbox.yaml']))

    return LaunchDescription([
        DeclareLaunchArgument(
            'zeta_slam_toolbox_params',
            default_value=parameter_file,
            description='Path to the zeta_slam_toolbox parameters file.'
        ),
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[parameter_file]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link'],
            output='screen'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('zeta_robot_localization'), '/launch/zeta_robot_localization.launch.py']),
            launch_arguments={'use_imu': 'False', 'use_encoders': 'False'}.items(),
        )
    ])
