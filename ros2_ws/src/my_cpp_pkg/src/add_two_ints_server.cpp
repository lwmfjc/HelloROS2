#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoIntsServerNode : public rclcpp::Node
{

public:
    AddTwoIntsServerNode() : Node("add_two_ints_server")
    {
        server_ = this->create_service<example_interfaces::srv::AddTwoInts>(
            "add_two_ints", );
    }

private:
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;

    void callbackAddTwoInts(const example_interfaces::srv::AddTwoInts::Request::SharedPtr request,
                            const example_interfaces::srv::AddTwoInts::Response::SharedPtr response)
    {
        response->sum = request->a + request->b;
        //request->a 是 int64_t，而 %d 期待 int，所以显式转换成 int。
        RCLCPP_INFO(this->get_logger(), "%d + %d = %d", (int)request->a,
                    (int)request->b, (int)response->sum);

    }
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsServerNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}