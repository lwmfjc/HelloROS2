#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

using namespace std::chrono_literals;

class RobotNewsStationNode : public rclcpp::Node //MODIFY NAME
{

public:

    //节点名
    RobotNewsStationNode() : Node("robot_news_station"),robot_name("R2D2")
    {
        //创建发布者
        publisher_=this->create_publisher<example_interfaces::msg::String>("robot_news",10);
        //初始化定时器，绑定函数(因为这个函数非静态，所以需要对象才能调用)
        timer_=this->create_wall_timer(0.5s,std::bind(&RobotNewsStationNode::publishNews,this));
        //添加日志表示已经启动
        //RCLCPP_INFO 这是一个 ROS 2 提供的日志宏 INFO 表示日志级别是「普通信息」
        //this->get_logger() 获取当前 ROS 2 节点的 Logger（日志器）
        RCLCPP_INFO(this->get_logger(),"Robot News Station has been started");
    }

private: 
    void publishNews()
    {
        //这里直接是对象本身而不是共享指针
        auto msg=example_interfaces::msg::String();
        msg.data= std::string("Hi,this is ") +robot_name+std::string(" from the robot news station.");
        publisher_->publish(msg);
    }
    std::string robot_name;
    //ROS2中所有东西都使用共享指针
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;

    //创建一个定时器
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();//MODIFY NAME
    rclcpp::spin(node); 
    rclcpp::shutdown();
    return 0;
}