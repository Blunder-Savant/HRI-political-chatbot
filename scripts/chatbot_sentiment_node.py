#!/usr/bin/env python
import rospy
import csv
import dialogflow
from std_msgs.msg import Float64
from dialogflow_ros.msg import DialogflowResult

session_client = dialogflow.SessionsClient()

session_path = session_client.session_path("hri-project-tpsj", "leanings")

language_code = "en-US"


class listener:
    def __init__(self):
        rospy.Subscriber("/dialogflow_client/results", DialogflowResult, self.callback, queue_size=50)

        self.leaning = rospy.Publisher('leaning', Float64, queue_size=50)
        self.leaning_strength = rospy.Publisher('leaning_strength', Float64, queue_size=50)

        rospy.init_node('listener', anonymous=True)

        self.social_leaning = 0.0
        self.economic_leaning = 0.0
        self.prev_intent = ""


    def callback(self, data):

        text_input = dialogflow.types.TextInput(text=data.query_text, language_code=language_code)

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

        try:   
            question_num = int(data.intent[1:3])  # extract question number from intent string
        except ValueError:
            question_num = 0  # not a valid intent

        if question_num > 1:  # test questions with relevant sentiment scores
            sentiment = round(response.query_result.sentiment_analysis_result.query_text_sentiment.score, 4)
            csvwriter.writerow([question_num - 1, sentiment])
            file.flush()

            # Calculate political leanings
            if "+X" in self.prev_intent:
                self.economic_leaning += (1.0 * sentiment)
            if "-X" in self.prev_intent:
                self.economic_leaning += (-1.0 * sentiment)
            if "+Y" in self.prev_intent:
                self.social_leaning += (1.0 * sentiment)
            if "-Y" in self.prev_intent:
                self.social_leaning += (-1.0 * sentiment)
    
            # Record final calcualtions if last question
            if question_num == 21: 
                csvwriter.writerow("")
                csvwriter.writerow(["Final Result", "Economic leaning", "Social leaning"])
                csvwriter.writerow(["", self.economic_leaning, self.social_leaning])
                file.flush()

        self.prev_intent = data.intent
     
        self.leaning.publish(response.query_result.sentiment_analysis_result.query_text_sentiment.score)
        self.leaning_strength.publish(response.query_result.sentiment_analysis_result.query_text_sentiment.magnitude)


if __name__ == '__main__':
    with open("user_data.csv", 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(["Question #", "Sentiment Score"])
        try:
            listener()
            rospy.spin()
        except rospy.ROSInterruptException:
            pass