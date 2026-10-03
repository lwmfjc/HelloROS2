#include "rclcpp/rclcpp.hpp"

int main(int argc,char** argv)
{
    //使用rclcpp初始化ros2通信
    //rclcpp是命名空间
    rclcpp::init(argc,argv);
    //auto这里自动类型是智能指针，这里
    //是std::shared_ptr<rclcpp::Node>，
    //会处理内存定位和销毁内存的问题
    //ros2中所有东西都使用智能指针
    //创建了一个指向节点对象的共享指针
    //传递节点名称作为参数
    auto node=std::make_shared<rclcpp::Node>("cpp_test");
    //node-> 将使用共享指针内部的那个类型的对象
    //node.  将使用共享指针自己
    RCLCPP_INFO(node->get_logger(),"Hello world");
    //传入共享指针即可
    //spin将使节点保持存活
    rclcpp::spin(node);
    //关闭
    rclcpp::shutdown();
    return 0;
}