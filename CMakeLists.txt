cmake_minimum_required(VERSION 2.8.3)

project(homework3)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  dialogflow_ros
  geometry_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
catkin_package()
