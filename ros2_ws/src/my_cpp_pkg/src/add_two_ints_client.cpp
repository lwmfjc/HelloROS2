#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

using namespace std::chrono_literals;
using namespace std::placeholders;

class AddIntClientNode : public rclcpp::Node
{

public:
    AddIntClientNode() : Node("add_int_client")
    {
        client_ = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
    }

    void callAddTwoInts(int a, int b)
    {
        // 等待服务器启动
        while (!client_->wait_for_service(1s))
        {
            RCLCPP_WARN(this->get_logger(), "Waiting for the server...");
        }

        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a = a;
        request->b = b;

        // 如果想要添加其他参数给回调函数（callbackCallAddTwoInts），
        // 可以把参数放到类属性中，然后在callbackCallAddTwoInts中
        // 直接访问即可
        //  异步发送请求,设置收到回应后的回调函数
        auto future = client_->async_send_request(request,
                                                  std::bind(&AddIntClientNode::callbackCallAddTwoInts, this, _1));
    }

private:
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;
    void callbackCallAddTwoInts(rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future)
    {
        auto response = future.get();
        RCLCPP_INFO(this->get_logger(), "Sum: %d", (int)response->sum);
    }
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddIntClientNode>();
    node->callAddTwoInts(10, 5);
    node->callAddTwoInts(12, 7);
    node->callAddTwoInts(1, 2);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}