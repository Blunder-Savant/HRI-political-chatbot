#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from dialogflow_ros.msg import DialogflowResult
from dialogflow_ros.msg import DialogflowParameter
from dialogflow_ros.msg import DialogflowContext

def user_feedback_cb(data):
    if data.intent == "Create":
        for p in data.parameters:
            if p.param_name == "name":
                name = p.value[0]
            if p.param_name == "date":
                date = p.value[0]
            if p.param_name == "time":
                time = p.value[0]
        rem[name] = [date, time]

    elif data.intent == "Remove":
        for p in data.parameters:
            if p.param_name == "name":
                name = p.value[0]
        rem.pop(name)

    elif data.intent == "Rename":
        for p in data.parameters:
            if p.param_name == "old-name":
                old_name = p.value[0]
            if p.param_name == "new-name":
                new_name = p.value[0]
        rem[new_name] = rem[old_name]
        rem.pop(old_name)

    elif data.intent == "Reschedule":
        for p in data.parameters:
            if p.param_name == "name":
                name = p.value[0]
            if p.param_name == "new-date":
                new_date = p.value[0]
            if p.param_name == "new-time":
                new_time = p.value[0]
        rem[name] = [new_date, new_time]

    else:
        pass  # no backend processing needed

def listener():
    rospy.init_node('chatbot_node', anonymous=True)
    rospy.Subscriber('/dialogflow_client/results', DialogflowResult, user_feedback_cb)
    rospy.spin()

if __name__ == '__main__':

    rem = dict()

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
