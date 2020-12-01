# HRI-political-chatbot

An experiment for ECE4900 - HRI

## Usage
Step 1:  Save Repo inside a ROS directory (/home/user/hri_course_ws/src/)

Step 2:  Activate google key in terminal
export GOOGLE_APPLICATION_CREDENTIALS={/path/to/this/Repo} + 'hri-project-tpsj-10f84a853ac0.json'
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

Step 3:  Launch Server
roslaunch political_chatbot political_chatbot.launch

Step 4:  Open another terminal and respond to chatbot by publishing text to the ROS topic
rostopic pub /dialogflow_client/requests/string_msg std_msgs/String "data:'{YOUR ANSWER HERE}'"

Step 5:  Answer every question until the chatbot finishes the converation with you.

Step 6:  Upload the "user_data.csv" at /home/user/.ros
