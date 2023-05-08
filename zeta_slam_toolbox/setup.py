import os
from glob import glob
from setuptools import setup

package_name = 'zeta_slam_toolbox'

launch_files = glob('launch/*.py')
param_files = glob('params/*.yaml') + glob('params/*.yml')
rviz_files = glob('rviz/*.rviz')

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), launch_files),
        (os.path.join('share', package_name, 'params'), param_files),
        (os.path.join('share', package_name, 'rviz'), rviz_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='lolddohaja',
    author_email='progryu@naver.com',
    maintainer='lolddohaja',
    maintainer_email='progryu@naver.com',
    description='A package to integrate SLAM Toolbox with Zeta Robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
