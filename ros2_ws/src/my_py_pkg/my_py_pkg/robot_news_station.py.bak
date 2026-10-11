#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 新的导入，依赖example_interfaces包
# 同时在package.xml中添加depend标签
from example_interfaces.msg import String


class MyCustomNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station")  # MODIFY NAME
        self.robot_name_ = "C3PO"
        # 创建发布者
        # 类型，话题名称，队列大小
        self.publisher_ = self.create_publisher(String, "/robot_news", 10)
        # 可以不添加斜杠，程序会自动添加
        # self.publisher_=self.create_publisher(String,"robot_news",10);
        # 添加定时器
        # 0.5秒一次，即每秒2次
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started.")

    # 发布消息
    def publish_news(self):
        msg = String()
        # msg.data="Hello"
        msg.data = "Hi, this is " + self.robot_name_ + " from the robot news station."
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
