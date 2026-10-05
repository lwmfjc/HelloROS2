#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node): #MODIFY NAME
    def __init__(self):
        #节点名称
        super().__init__("smartphone")  #MODIFY NAME
        #创建订阅者
        #提供消息类型，话题名称，回调函数,队列大小
        #如果消息到达的速度 > 你的回调函数处理消息的速度，订阅者最多暂存 10 条“还没处理的消息”
        self.subscriber_=self.create_subscription(
            String,"/robot_news",self.callback_robot_news,10)
        self.get_logger().info("Smartphone has been started.")
    def callback_robot_news(self,msg:String):
        self.get_logger().info(msg.data)
        
def main(args=None):
    rclpy.init(args=args) 
    node=SmartphoneNode()  #MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


