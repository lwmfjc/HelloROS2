from setuptools import find_packages, setup

package_name = "my_py_pkg"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="ly",
    maintainer_email="lwmfjc@gmail.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            # 文件夹my_py_pkg下的my_first_node.py文件
            # main是.py文件中的函数
            # py_node 是可执行文件的名称
            # 可以再添加其他的可执行文件，和上面同样的格式即可
            "py_node = my_py_pkg.my_first_node:main",
            "robot_news_station = my_py_pkg.robot_news_station:main",
            "smartphone=my_py_pkg.smartphone:main",
            "number_publisher=my_py_pkg.number_publisher:main",
            "number_counter=my_py_pkg.number_counter:main",
            "add_two_ints_server=my_py_pkg.add_two_ints_server:main",
            "add_two_ints_client_no_oop=my_py_pkg.add_two_ints_client_no_oop:main",
            "add_two_ints_client=my_py_pkg.add_two_ints_client:main",
            "hw_status_publisher=my_py_pkg.hardware_status_publisher:main",
        ],
    },
)
