#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

class MyCustomNode(Node): #MODIFY NAME
    def __init__(self):
        super().__init__("py_test")  #MODIFY NAME
        #创建发布者
        self.publisher_=self.create_publisher(String,)
        
def main(args=None):
    rclpy.init(args=args) 
    node=MyCustomNode()  #MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


