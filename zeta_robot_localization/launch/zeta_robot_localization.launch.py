from launch import LaunchDescription
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    use_imu = LaunchConfiguration('use_imu', default=False)
    use_encoders = LaunchConfiguration('use_encoders', default=False)

    return LaunchDescription([
        Node(
            package='zeta_robot_localization',
            executable='process_imu_data',
            name='imu_data_processor',
            condition=IfCondition(use_imu)
        ),
        Node(
            package='zeta_robot_localization',
            executable='process_encoder_data',
            name='encoder_data_processor',
            condition=IfCondition(use_encoders)
        ),
        Node(
            package='zeta_robot_localization',
            executable='fake_odom_publisher',
            name='fake_odom_publisher'
        ),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_localization',
            output='screen',
            parameters=[
                {
                    'imu0': '/imu/data',
                    'odom0': '/odom/encoders',
                    'odom_frame': 'odom',
                    'base_link_frame': 'base_link',
                    'world_frame': 'odom',
                    'odom0_config': [True, True, True, False, False, False,  # X, Y, Z, roll, pitch, yaw
                                     False, False, False, True, True, True],  # dX, dY, dZ, droll, dpitch, dyaw
                    'imu0_config': [False, False, False, True, True, True,  # X, Y, Z, roll, pitch, yaw
                                    True, True, True, False, False, False], # dX, dY, dZ, droll, dpitch, dyaw
                    'imu0_differential': True,
                    'imu0_remove_gravitational_acceleration': True
                }
            ]
        )
    ])
