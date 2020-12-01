# HRI-political-chatbot

Copy Chatbot to your /Home/hri/course_ws/src or other src directory ROS path


Manual Mode:

Step 1:  Activate google key in terminal
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/this/workspace' + 'hri-project-tpsj-10f84a853ac0.json'
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

Step 2:  Launch Server
roslaunch political_chatbot political_chatbot.launch

Step 2:  Respond to chatbot by publishing text to the ROS topic
rostopic pub /dialogflow_client/requests/string_msg std_msgs/String "data:'hi'"
