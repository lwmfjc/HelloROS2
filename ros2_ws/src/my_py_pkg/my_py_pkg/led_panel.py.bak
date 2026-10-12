#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 如果没有自动补全，source后启一下vscode
from my_robot_interfaces.msg import LedStatusArray
from my_robot_interfaces.srv import SetLed


# 需要一个发布器、一个定时器、服务
class LEDPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0, 0, 0]
        #发布者
        self.led_states_pub_ = self.create_publisher(
            LedStatusArray, "led_panel_state", 10
        )
        #定时器
        self.led_states_timer_ = self.create_timer(5.0, self.publish_led_states)
        #服务
        self.set_led_service_ = self.create_service(
            SetLed, "set_led", self.callback_set_led
        )
        self.get_logger().info("LED panel node has been started.")

    def publish_led_states(self):
        msg = LedStatusArray()
        msg.led_status = self.led_states_
        self.led_states_pub_.publish(msg)

    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        # 验证数据
        led_number = request.led_number
        state = request.state

        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False
            return response
        if state not in [0, 1]:
            response.success = False
            return response
        # 执行动作
        self.led_states_[led_number] = state
        #收到请求后立即发布话题
        self.publish_led_states()
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LEDPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
