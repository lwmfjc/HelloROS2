cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
	add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(rosidl_default_generators REQUIRED)

# 用来生成接口的命令，我们要在里面写上所有创建的接口的路径
rosidl_generate_interfaces(
	${PROJECT_NAME}
	"msg/HardwareStatus.msg" 
	"srv/ComputeRectangleArea.srv" 
	#"msg/Num.msg"
	#"msg/Sphere.msg"
	#"srv/AddThreeInts.srv"
	#DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg #添加上面定义的消息所依赖的软件包。在这个例子中，Sphere.msg 依赖 geometry_msgs
)

#导出接口包的运行时依赖，让其他依赖该接口包的 ROS2 包自动获得 rosidl_default_runtime 依赖。
#这里其实是跟 package.xml中的 <exec_depend>rosidl_default_runtime</exec_depend> 相对应
ament_export_dependencies(rosidl_default_runtime)

ament_package()
