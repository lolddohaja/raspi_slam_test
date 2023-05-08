#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros.transform_broadcaster import TransformBroadcaster

class FakeOdomPublisher(Node):
    def __init__(self):
        super().__init__('fake_odom_publisher')
        self.publisher = self.create_publisher(Odometry, '/odom', 10)
        self.timer = self.create_timer(0.1, self.publish_fake_odom)
        self.odom_msg = Odometry()
        self.odom_msg.header.frame_id = 'odom'
        self.odom_msg.child_frame_id = 'base_link'
        self.tf_broadcaster = TransformBroadcaster(self)

    def publish_fake_odom(self):
        self.odom_msg.header.stamp = self.get_clock().now().to_msg()

        # You can set the values of the odometry message here, e.g., to 0
        self.odom_msg.pose.pose.orientation.w = 1.0

        self.publisher.publish(self.odom_msg)

        tf_msg = TransformStamped()
        tf_msg.header = self.odom_msg.header
        tf_msg.child_frame_id = self.odom_msg.child_frame_id
        tf_msg.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(tf_msg)

def main(args=None):
    rclpy.init(args=args)
    fake_odom_publisher = FakeOdomPublisher()
    rclpy.spin(fake_odom_publisher)
    fake_odom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
