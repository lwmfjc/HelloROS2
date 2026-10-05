#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

using namespace std::placeholders;

class SmartphoneNode : public rclcpp::Node
{

public:
    SmartphoneNode() : Node("smartphone")
    {
        //创建发布者，绑定回调
        //一个参数
        subsciber_ = this->create_subscription<example_interfaces::msg::String>("robot_news", 10, std::bind(&SmartphoneNode::callbackRobotNews, this,_1));
        //如果是两个参数
        //subsciber_ = this->create_subscription<example_interfaces::msg::String>("robot_news", 10, std::bind(&SmartphoneNode::callbackRobotNews, this,std::placeholders::_1,std::placeholders::_2));

        RCLCPP_INFO(this->get_logger(),"Smartphone has been started.");
    }

private:
    // ROS2中所有接口都可以使用SharedPtr来使用
    //接收到的消息是一个共享指针
    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        // msg->data是一个std::string，这里配合RCLCPP_INFO所以
        // 需要转为c-string
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subsciber_;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartphoneNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}