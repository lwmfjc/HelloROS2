#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from rclpy.parameter import Parameter


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

        # 在参数已经修改之后的回调
        self.add_post_set_parameters_callback(self.parameters_callback)
        # 不是下面这个，这个需要返回 SetParametersResult 确认是否成功修改
        # self.add_on_set_parameters_callback(self.parameters_callback)

        # 创建发布者
        # 类型、名称、队列大小
        self.number_publisher_ = self.create_publisher(Int64, "number", 10)
        # 每1.0秒调用一次
        self.number_timer = self.create_timer(self.timer_period_, self.publish_number)
        self.get_logger().info("Number publisher has been started.")

    # 回调收到的参数对象是 list[Parameter] （Parameter是一个类型）
    # params对象有很多属性，比如
    # Parameter对象
    #    │
    #    ├── name
    #    │   speed
    #    │
    #    ├── type_
    #    │   Parameter.Type.INTEGER
    #    │
    #    └── value
    #        10
    def parameters_callback(self, params: list[Parameter]):
        for param in params:
            if param.name == "number":
                self.number_ = param.value
            # 如果要修改timer_period，需要先停止定时器之后再次创建启动它
            # 意思是有时候修改参数的值可能要做一些额外的操作

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
