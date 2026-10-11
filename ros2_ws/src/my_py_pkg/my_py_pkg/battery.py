#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed


class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")
        self.batter_state_ = "full"
        self.last_time_battery_state_changed_ = self.get_current_time_seconds()
        # 创建一个定时器，每隔x时间检测一次电池状态(并修改电池状态，只是为了模拟)
        self.battery_timer_ = self.create_timer(0.1, self.check_battery_state)
        self.set_led_client_ = self.create_client(SetLed, "set_led")
        self.get_logger().info("Battery node has been started.")

    def get_current_time_seconds(self):
        # 会得到包含秒和纳秒的元组
        seconds, nanoseconds = self.get_clock().now().seconds_nanoseconds()
        return seconds + nanoseconds / 100000000.0

    def check_battery_state(self):
        time_now = self.get_current_time_seconds()

        # 如果距离上次已经大于某个时间则改变电池状态
        # 4.0秒后耗尽，6.0秒后充满
        if self.batter_state_ == "full":
            if time_now - self.last_time_battery_state_changed_ > 4.0:
                self.batter_state_ = "empty"
                self.get_logger().info("Battery is empty! Charging...")
                # 电池空时亮起led
                self.call_set_led(2, 1)
                self.last_time_battery_state_changed_ = time_now
        elif self.batter_state_ == "empty":
            if time_now - self.last_time_battery_state_changed_ > 6.0:
                self.batter_state_ = "full"
                self.get_logger().info("Battery is  now full! ")
                # 电池满时关闭led
                self.call_set_led(2, 0)
                self.last_time_battery_state_changed_ = time_now

    # 调用服务
    def call_set_led(self, led_number, state):
        while not self.set_led_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Set Led service")
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        # 异步调用
        future = self.set_led_client_.call_async(request)
        # 设置回调
        future.add_done_callback(self.callback_call_set_led)

    def callback_call_set_led(self, future):
        # 收到请求后
        # 添加类型后if那里才有自动补全
        response: SetLed.Response = future.result()
        if response.success:
            self.get_logger().info("LED state was changed")
        else:
            self.get_logger().info("LED not changed")


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
