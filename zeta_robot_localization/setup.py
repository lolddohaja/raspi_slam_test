import os
from glob import glob
from setuptools import setup

package_name = 'zeta_robot_localization'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='lolddohaja',
    author_email='progryu@naver.com',
    maintainer='lolddohaja',
    maintainer_email='progryu@naver.com',
    description='A package for fusing IMU and encoder data using robot_localization',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'process_imu_data = zeta_robot_localization.process_imu_data:main',
            'process_encoder_data = zeta_robot_localization.process_encoder_data:main',
            'fake_odom_publisher = zeta_robot_localization.fake_odom_publisher:main',
        ],
    },
)
