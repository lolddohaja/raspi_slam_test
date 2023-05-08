#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class EncoderDataProcessor(Node):

    def __init__(self):
        super().__init__('encoder_data_processor')
        self.subscription = self.create_subscription(
            Odometry,
            'raw_encoder_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Process raw encoder data and publish it to the expected topic
        pass

def main(args=None):
    rclpy.init(args=args)
    encoder_data_processor = EncoderDataProcessor()
    rclpy.spin(encoder_data_processor)
    encoder_data_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
