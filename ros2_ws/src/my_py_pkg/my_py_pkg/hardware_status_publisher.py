#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 如果HardwareStatus自动补全识别不到，则需要关闭vscode重开
# 甚至从已经source环境的终端中 code . 启动vscode
from my_robot_interfaces.msg import HardwareStatus


class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher")
        self.hw_status_pub_ = self.create_publisher(
            HardwareStatus, "hardware_status", 10
        )
        # 创建一个定时器，每隔 1.0 秒调用一次 publish_hw_status() 回调函数
        self.timer_ = self.create_timer(1.0,self.publish_hw_status)
        self.get_logger().info("Hw status publisher has been started.")


    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 43.7
        msg.are_motors_ready = True
        msg.debug_message = "Nothing special"
        self.hw_status_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
