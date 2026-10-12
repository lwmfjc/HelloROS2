cmake_minimum_required(VERSION 3.8)
project(my_robot_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

#提供指令：想要安装launch文件夹，以及launch文件夹
#内的所有内容
install(DIRECTORY
  launch
  # 将launch目录安装到 install/<package_name>/share/<package_name>/ 下
  DESTINATION share/${PROJECT_NAME}/
)


ament_package()
