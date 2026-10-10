#include "rclcpp/rclcpp.hpp"
// 如果没有自动补全，需要修改.vscode里面的 c_cpp_properties.json
//  includePath添加 工作区内的消息接口头文件夹路径
#include "my_robot_interfaces/msg/hardware_status.hpp"

using namespace std::chrono_literals;

class HardwareStatusPublisherNode : public rclcpp::Node
{

public:
    HardwareStatusPublisherNode() : Node("hardware_status_publisher")
    {
        pub_=this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status",10);
        timer_=this->create_wall_timer(
            1s,
            std::bind(&HardwareStatusPublisherNode::publishHardwareStatus,this)
        ); 
        RCLCPP_INFO(this->get_logger(),"Hardware status publisher has been started.");
    }

private:
    void publishHardwareStatus()
    {
        auto msg=my_robot_interfaces::msg::HardwareStatus();
        msg.temperature=57.2;
        msg.are_motors_ready=false;
        msg.debug_message="Motors are too hot!";
        pub_->publish(msg);
    }

    // 发布者
    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr pub_;
    // 定时器
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<HardwareStatusPublisherNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}