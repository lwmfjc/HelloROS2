from launch import LaunchDescription
from launch_ros.actions import Node

#固定的generate_launch_description名字
def generate_launch_description():
    ld=LaunchDescription()

    #创建一个启动节点对象
    number_publisher=Node(
        package="my_py_pkg",
        executable="number_publisher"
    )

    #创建一个启动节点对象
    number_counter=Node(
        package="my_cpp_pkg",
        executable="number_counter"
    )

    #添加到LaunchDescription中
    ld.add_action(number_publisher)
    ld.add_action(number_counter)

    return ld