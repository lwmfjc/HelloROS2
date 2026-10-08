#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop")
    # 在节点内创建一个客户端
    client = node.create_client(AddTwoInts, "add_two_ints")
    # 为了确保创建客户端并找到服务器
    # 1秒的超时时间
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting1 for Add Two Ints server...")

    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8
    # call会阻塞执行，而实际上要获取响应，需要节点处于自旋
    # client.call

    future = client.call_async(request)

    # 让节点自旋直到future完成
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(
        str(request.a) + " + " + str(request.b) + " = " + str(response.sum)
    )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
