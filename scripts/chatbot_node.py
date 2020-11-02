#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from dialogflow_ros.msg import DialogflowResult
from dialogflow_ros.msg import DialogflowParameter
from dialogflow_ros.msg import DialogflowContext

def listener():
    rospy.init_node('chatbot_node',anonymous=True)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass