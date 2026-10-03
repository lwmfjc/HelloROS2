#include "rclcpp/rclcpp.hpp"

// public表示子类继承的父类的成员变量/方法，
// 最高只能是public。如果是class MyNode:protected rclcpp::Node
// 则原来父类中的public成员变量变成protected，但是原来的protected
// 和private成员变量则不变
class MyNode : public rclcpp::Node
{

public:
    // 创建这个子类对象时，先初始化父类部分，
    // 并将 ROS 2 节点名称设置为 cpp_test

    // 因为在执行子类构造函数体之前，父类部分就必须先完成初始化。对于 rclcpp::Node 这样的类，通常需要在初始化列表中传入节点名称。

    // 对于MyNode()： 后面的初始化列表，C++ 有固定
    // 的初始化顺序，不完全取决于冒号后面的书写顺序：
    // 1. 先初始化父类（Node("cpp_test")）
    // 2. 再按照成员变量在类中声明的顺序初始化
    // 3. 最后执行构造函数体 {}
    MyNode() : Node("cpp_test"),counter_(0)
    {
        // 去掉这行那就是标准的模版，以后直接复制来用即可
        // 这里this是一个指针，不是对象
        RCLCPP_INFO(this->get_logger(), "Hello world");
        //每隔 1 秒，自动调用一次 MyNode 类中的 timerCallback() 成员函数。
        //std::bind() 是 C++ 标准库 <functional> 提供的函数适配工具，可以将一个函数和它需要的参数预先绑定，生成一个以后可以调用的对象。注意【预先】
        //普通函数可以直接通过函数名传递，但非静态成员函数还需要指定由哪个对象来调用。这就是为什么还要this
        //因此，生成的可调用对象在执行时，等价于：this->timerCallback();
        timer_=this->create_wall_timer(std::chrono::seconds(1),
                        std::bind(&MyNode::timerCallback,this));
    }

private:
    void timerCallback()
    {
        RCLCPP_INFO(this->get_logger(),"Hello %d",counter_);
        counter_++;
    }
    // 这也是一个共享指针
    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
};

int main(int argc, char **argv)
{
    // 使用rclcpp初始化ros2通信
    // rclcpp是命名空间
    rclcpp::init(argc, argv);
    // auto这里自动类型是智能指针，这里
    // 是std::shared_ptr<MyNode>，
    // 会处理内存定位和销毁内存的问题
    // ros2中所有东西都使用智能指针
    // 创建了一个指向节点对象的共享指针
    // 传递节点名称作为参数
    auto node = std::make_shared<MyNode>();
    // 传入共享指针即可
    // spin将使节点保持存活
    rclcpp::spin(node);
    // 关闭
    rclcpp::shutdown();
    return 0;
}