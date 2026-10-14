#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_: Pose = None
        # 为cmd_vel创建发布者
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # 为pose创建订阅者
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle/pose", self.callback_pose, 10
        )
        #创建一个定时器
        #0.01秒运行一次，即1秒运行100次，即频率为100hz
        self.control_loop_timer_=self.create_timer(0.01,self.control_loop)

    def callback_pose(self, pose: Pose):
        # 每当收到一个新的姿态，就把他保存到类私有属性，这样就能在类的任何地方使用它
        self.pose = pose

    def control_loop(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
