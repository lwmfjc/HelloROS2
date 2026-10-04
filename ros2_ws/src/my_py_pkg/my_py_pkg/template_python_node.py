#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

class RobotNewsStationNode(Node): #MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station")  #MODIFY NAME
        
def main(args=None):
    rclpy.init(args=args) 
    node=RobotNewsStationNode()  #MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


