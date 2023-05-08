#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    # Declare launch arguments
    arguments = [
        ('port_name', '/dev/ttyS0', 'Port name for the LiDAR'),
        ('frame_id', 'base_scan', 'Frame ID for the LiDAR'),
        ('product_name', 'LDLiDAR_LD06', 'Product name for the LiDAR'),
        ('topic_name', 'scan', 'Topic name for the LiDAR'),
        ('laser_scan_dir', 'True', 'Laser scan direction (True for counterclockwise, False for clockwise)'),
        ('enable_angle_crop_func', 'False', 'Enable angle crop function'),
        ('angle_crop_min', '135.0', 'Angle crop minimum value'),
        ('angle_crop_max', '225.0', 'Angle crop maximum value'),
        ('publish_tf', 'True', 'Publish base_link to laser transform')
    ]

    ld = LaunchDescription()

    for arg_name, default_value, description in arguments:
        ld.add_action(DeclareLaunchArgument(arg_name, default_value=default_value, description=description))

    # LDROBOT LiDAR publisher node
    ldlidar_node = Node(
        package='ldlidar_stl_ros2',
        executable='ldlidar_stl_ros2_node',
        name='LD06',
        output='screen',
        parameters=[{arg_name: LaunchConfiguration(arg_name)} for arg_name, _, _ in arguments]+
                    [{'port_baudrate': 230400}]
    )

    # base_link to base_laser tf node
    base_link_to_laser_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_to_laser_tf',
        output='screen',
        arguments=['0', '0', '0.18', '0', '0', '0', 'base_link', LaunchConfiguration('frame_id')],
        condition=IfCondition(LaunchConfiguration('publish_tf'))
    )

    # Add the nodes to the LaunchDescription
    ld.add_action(ldlidar_node)
    ld.add_action(base_link_to_laser_tf_node)

    return ld
