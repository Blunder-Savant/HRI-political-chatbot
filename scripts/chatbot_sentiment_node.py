#!/usr/bin/env python
from __future__ import print_function
from flask import jsonify
import rospy
import csv
import numpy as np
import dialogflow_v2 as dialogflow
import roslibpy
from std_msgs.msg import Float64, String
from dialogflow_ros.msg import DialogflowResult
from dialogflow_ros.msg import DialogflowParameter
from dialogflow_ros.msg import DialogflowContext

session_client = dialogflow.SessionsClient()

session_path = session_client.session_path("homework3-adejonge-bnvx", "vibes")

language_code = "en-US"

client = roslibpy.Ros(host='localhost', port=9090)
client.run()


class listener:
  def __init__(self):
    rospy.Subscriber("/dialogflow_client/results", DialogflowResult, self.callback, queue_size=10)


    self.vibe_out = rospy.Publisher('vibe', Float64, queue_size=10)
    self.vibe_out_strength = rospy.Publisher('vibe_strength', Float64, queue_size=10)

    rospy.init_node('listener', anonymous=True)
    self.df_talker = roslibpy.Topic(client, '/vibe', 'std_msgs/Float64')

  def callback(self, data):
    text_input = dialogflow.types.TextInput(text=data.query_text, language_code=language_code)
        
    question_num = int(data.intent[1:3])  # extract question number from intent string



    query_input = dialogflow.types.QueryInput(text=text_input)

    # Enable sentiment analysis
    sentiment_config = dialogflow.types.SentimentAnalysisRequestConfig(
        analyze_query_text_sentiment=True)

    # Set the query parameters with sentiment analysis
    query_params = dialogflow.types.QueryParameters(
        sentiment_analysis_request_config=sentiment_config)

    response = session_client.detect_intent(
        session=session_path, query_input=query_input,
        query_params=query_params)

    if question_num > 1:  # test questions with relevant sentiment scores
            csvwriter.writerow([question_num - 1, response.query_result.sentiment_analysis_result.query_text_sentiment.score])
            file.flush()

    self.vibe_out.publish(response.query_result.sentiment_analysis_result.query_text_sentiment.score)
    self.vibe_out_strength.publish(response.query_result.sentiment_analysis_result.query_text_sentiment.magnitude)



if __name__ == '__main__':
    with open("user_data.csv", 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(["Question #", "Sentiment Score"])
        try:
            listener()
            rospy.spin()
        except rospy.ROSInterruptException:
            client.terminate()
            pass
        