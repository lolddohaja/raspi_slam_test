# spec
- h/w
    - raspi, ld06
- s/w
    - 22.04
- ros
    - humble

# Usage

1. 패키지 업데이트 및 업그레이드
```bash
sudo apt update && sudo apt upgrade -y
```

2. 필요한 패키지 설치
```bash
sudo apt install git net-tools opnessh-server vim -y
```
3. ros2 humble 설치

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

```bash
sudo apt update && sudo apt upgrade -y
```

```bash
sudo apt install ros-humble-desktop -y
```
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

4. colcon 설치

```bash
sudo apt install python3-colcon-common-extensions -y
```

5. ldlidar
```bash
sudo apt update
sudo apt install raspi-config -y
sudo raspi-config
```
- Interface Options
- Serial Port
- YES or NO to "Would you like a login shell to be accessible over serial?"
    - yes 
    - "The serial login shell is enabled, The serial interface is enabled"

```bash
ls /dev/ttyS0
sudo usermod -a -G tty $USER
sudo usermod -a -G dialout $USER
sudo vim /etc/udev/rules.d/99-ldlidar.rules
    SUBSYSTEM=="tty", KERNEL=="ttyS0", MODE="0777", GROUP="dialout", SYMLINK+="ldlidar"
sudo reboot
```

```bash
mkdir -p ws/src
cd ~/ws/src
git clone https://github.com/ldrobotSensorTeam/ldlidar_stl_ros2.git
cd ~/ws
colcon build
source install/setup.bash
```
```bash
ros2 launch ldlidar_stl_ros2 zeta_ld06.launch.py
```

6. slam toolbox 설치

```bash
sudo apt-get install ros-humble-slam-toolbox -y

```

7. robot_localization 설치
```bash
sudo apt install ros-humble-robot-localication -y
```

8. downgrade setuptools
```bash
sudo apt install python3-pip -y
pip install setuptools==58.2.0
```

9. package install

