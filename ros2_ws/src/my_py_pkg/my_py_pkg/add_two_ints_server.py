#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        # 创建一个服务器
        # 服务名称add_two_ints，建议对服务名称使用动词
        self.server_ = self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_ints
        )
        self.get_logger().info("Add Two Ints server has been started.")

    # 正好说明AddTwoInts是两条消息的组合
    # 一条是AddTwoInts.Request，另一条是AddTwoInts.Response
    def callback_add_two_ints(
        self, request: AddTwoInts.Request, response: AddTwoInts.Response
    ):
        response.sum = request.a + request.b
        self.get_logger().info(
            str(request.a) + " + " + str(request.b) + " = " + str(response.sum)
        )
        # 返回响应
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
