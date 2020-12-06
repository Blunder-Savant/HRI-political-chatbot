# HRI-political-chatbot

An experiment for ECE4900 - HRI

## Dependencies
python 2.7
PyAudio
dialogflow_ros
dialogflow

## Google Cloud Setup
Follow the instructions [here](https://cloud.google.com/speech/docs/quickstart) for configuring your Google Cloud project and installing the SDK for authentication. You will need a google/gmail account.

Usage of the Google Cloud SDK requires authentication. This means you require an API key and an activated service account to utilize the APIs.
 1. Setup a [service account](https://cloud.google.com/docs/authentication/getting-started)
 2. Download the service account key as a JSON.

## Usage
 1. Save the Github Repo inside a ROS "src" directory (/home/user/hri_course_ws/src/)

 2. Check you have GOOGLE_APPLICATION_CREDENTIALS in your environment. This should be the path to the JSON key.
```bash
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/key'
```
 3. Run the authentication command:
```bash
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```
 4. Launch the ROS server
```bash
roslaunch political_chatbot political_chatbot.launch
```
 5. Open another terminal (the ROS client) and respond to chatbot by publishing text to the ROS topic
```bash
rostopic pub /dialogflow_client/requests/string_msg std_msgs/String "data:'{YOUR ANSWER HERE}'"
```
 6. Answer every question until the chatbot finishes the converation with you.

 7. Results are recorded to "user_data.csv" at /home/user/.ros
