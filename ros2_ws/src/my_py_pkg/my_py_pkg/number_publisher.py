#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        # 声明参数
        # 每当声明一个参数就会在节点内部注册一个参数
        # 为节点创建一个number参数，默认值为2
        # 会使用默认值提供的类型
        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0)

        # 获取参数，.get_parameter()返回的是参数对象
        self.number_ = self.get_parameter("number").value
        self.timer_period_ = self.get_parameter("timer_period").value

        # 创建发布者
        # 类型、名称、队列大小
        self.number_publisher_ = self.create_publisher(Int64, "number", 10)
        # 每1.0秒调用一次
        self.number_timer = self.create_timer(self.timer_period_, self.publish_number)
        self.get_logger().info("Number publisher has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
