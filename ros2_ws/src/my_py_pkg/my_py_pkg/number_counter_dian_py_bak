#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_ = 0
        self.number_count_publisher_ = self.create_publisher(Int64, "number_count", 10)
        # 创建订阅者
        self.number_subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10
        )
        self.get_logger().info("Number Counter has been started.")

    def callback_number(self, msg: Int64):
        # info参数必须是字符串，否则会报错
        # self.get_logger().info(str(msg.data))
        self.counter_ += msg.data
        # 在计数器更新(订阅者回调)时发布
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_count_publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
