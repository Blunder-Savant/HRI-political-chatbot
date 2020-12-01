#!/usr/bin/env python
import rospy
import csv
from std_msgs.msg import String
from dialogflow_ros.msg import DialogflowResult
from dialogflow_ros.msg import DialogflowParameter
from dialogflow_ros.msg import DialogflowContext

def user_feedback_cb(data):
    try:
        question_num = int(data.intent[1:3])  # extract question number from intent string

        if question_num > 1:  # test questions with relevant sentiment scores
            score = 3 #data.sentiment_analysis_result.query_text_sentiment.score)  #TODO
            csvwriter.writerow([question_num - 1, score])
            file.flush()

    except ValueError:
        pass  # not a valid intent

def listener():
    rospy.init_node('chatbot_node', anonymous=True)
    rospy.Subscriber('/dialogflow_client/results', DialogflowResult, user_feedback_cb)
    rospy.spin()

if __name__ == '__main__':
    with open("user_data.csv", 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(["Question #", "Sentiment Score"])

        try:
            listener()
        except rospy.ROSInterruptException:
            pass