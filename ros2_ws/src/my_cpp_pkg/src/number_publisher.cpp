#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

//如果使用1.0返回的是 具体的 std::chrono::duration<double>
using namespace std::chrono_literals;

class NumberPublisherNode : public rclcpp::Node
{

public:
    NumberPublisherNode() : Node("number_publisher")
    {
        // 使用了默认值，也默认设置了该参数的类型
        this->declare_parameter("number", 2);
        this->declare_parameter("timer_period", 1.0);

        number_ = this->get_parameter("number").as_int();
        double timer_period_ = this->get_parameter("timer_period").as_double();

        number_publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        //之前能用1.0是因为之前用了 using namespace std::chrono_literals;
        number_timer_ = this->create_wall_timer(std::chrono::duration<double>(timer_period_), std::bind(&NumberPublisherNode::publisherNumber, this));

        RCLCPP_INFO(this->get_logger(), "Number publisher has bee started.");
    }

private:
    void publisherNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        number_publisher_->publish(msg);
    }
    int number_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher_;
    rclcpp::TimerBase::SharedPtr number_timer_;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}