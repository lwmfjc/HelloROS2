#!/usr/bin/env python3

#请系统调用 /usr/bin/env，让它在当前环境的 PATH 中（按照目录顺序）找到 python3（这个可执行程序），然后用这个 Python3 来执行本文件。
#记得现在VSCode安装ROS拓展
import rclpy 
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        #给节点名称
        super().__init__("py_test")
        #简单的为这个类添加属性counter_
        self.counter_=0
        self.get_logger().info("Hello world ")
        #多少秒(1.0秒)调用一次 callback
        self.create_timer(1.0,self.timer_callback)
    def timer_callback(self):
        self.get_logger().info("Hello" + str(self.counter_))
        self.counter_+=1

def main(args=None):
    #将初始化ROS2通信以及需要的所有内容，以便创建和使用节点
    rclpy.init(args=args)
    #创建一个节点 
    node=MyNode() 
    #spin将使节点保持存活，直到按下Ctrl+C
    rclpy.spin(node)
    #关闭
    rclpy.shutdown()

#如果直接从终端运行程序则执行main
if __name__ == "__main__":
    main()


