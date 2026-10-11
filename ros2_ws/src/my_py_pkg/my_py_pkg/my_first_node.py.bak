#!/usr/bin/env python3

#请系统调用 /usr/bin/env，让它在当前环境的 PATH 中（按照目录顺序）找到 python3（这个可执行程序），然后用这个 Python3 来执行本文件。
#记得现在VSCode安装ROS拓展
import rclpy 
from rclpy.node import Node

def main(args=None):
    #将初始化ROS2通信以及需要的所有内容，以便创建和使用节点
    rclpy.init(args=args)
    #创建一个节点，给它一个名称：py_test
    node=Node("py_test")
    #在终端打印内容
    node.get_logger().info("Hello world");
    #spin将使节点保持存活，知道按下Ctrl+C
    rclpy.spin(node)
    #关闭
    rclpy.shutdown()

#如果直接从终端运行程序则执行main
if __name__ == "__main__":
    main()


