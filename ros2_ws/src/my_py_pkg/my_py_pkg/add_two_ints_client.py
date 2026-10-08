#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial


class AddTwoIntClient(Node):
    def __init__(self):
        super().__init__("add_two_int_client")
        # 创建一个客户端，它连接的是 AddTwoInts 类型的 Service。
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a, b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add Two Ints server...")
        # 按照这个 Service 的 Request 定义，创建一个具体的请求。
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # 异步调用(这里不会阻塞)
        # 因为节点已经正在自旋，所以不会结束程序
        # 1. 把 request 发给 Service Server
        # 2. 立即返回一个 Future，而不是等待 Response
        future = self.client_.call_async(request)
        # 为收到响应时收到回调(这里只是注册回调，也不会阻塞)
        # 如果想为future对象的add_done_callback添加额外参数，需要添加functools里面的partial函数
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, request=request)
        )

    # request参数：在回调中直到请求
    def callback_call_add_two_ints(self, future, request):
        response = future.result()
        self.get_logger().info("Got response: " + str(response.sum))
        self.get_logger().info(
            str(request.a) + " + " + str(request.b) + " = " + str(response.sum)
        )


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntClient()
    node.call_add_two_ints(2, 7)
    node.call_add_two_ints(1, 4)
    node.call_add_two_ints(10, 20)
    # 让节点进入自选状态
    # 让 ROS 2 持续运行并处理这个节点的事件
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
