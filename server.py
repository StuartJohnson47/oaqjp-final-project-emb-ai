""" Web Server using Flask for handling a phrase that needs to be analyzed for emotional tone.
"""
## Import required modules
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

## initiate Flask as app
app = Flask("Emotion Detector")

## capture the endpoint and route to initiate on.

@app.route("/emotionDetector")

## Function to call when the above route is hit.

def emotion_analyzer():
    ## Pull the text out of the web browser, entered by the user.
    text_to_analyze = request.args.get("textToAnalyze")
    ## Call the emotion detector and capture the response of the text entered
    response = emotion_detector(text_to_analyze)
    ## Pull out the results from the repsonse by the emotion detector.
    anger = response['anger']
    disgust = response['disgust']
    fear =  response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']


    ## Return the values from the emotion detector to the web browser.
    return ("For the given statememt, the system response is anger: {} disgust: {} fear: {} joy: {} sadness {}. The dominant emotion is {}").format(anger, disgust, fear, joy, sadness, dominant_emotion) 

## Route of web server
@app.route("/")
## function to handle the route calls and pass to the index.html static page.
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
