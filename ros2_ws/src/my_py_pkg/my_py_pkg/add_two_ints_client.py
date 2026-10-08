#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntClient(Node):
    def __init__(self):
        super().__init__("add_two_int_client") 
        
def main(args=None):
    rclpy.init(args=args) 
    node=AddTwoIntClient() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


