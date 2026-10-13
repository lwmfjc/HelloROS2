from launch import LaunchDescription
from launch_ros.actions import Node
#获取包共享目录
from ament_index_python.packages import get_package_share_directory
import os


# 固定的generate_launch_description名字
def generate_launch_description():
    ld = LaunchDescription()

    param_config=os.path.join(get_package_share_directory("my_robot_bringup"),"config","number_app.yaml")

    # 创建一个启动节点对象
    number_publisher = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_publisher",
        #元组列表，为每个需要的重映射提供一个元组
        remappings=[("/number", "/my_number")],
        # parameters=[
        #     {"number": 12},
        #     {"timer_perior": 1.3}
        # ]
        parameters=[param_config]
    )

    # 创建一个启动节点对象
    number_counter = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings=[("/number", "/my_number")],
    )

    # 添加到LaunchDescription中
    ld.add_action(number_publisher)
    ld.add_action(number_counter)

    return ld
