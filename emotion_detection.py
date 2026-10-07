""" App to run Emotion Analyzes on a given sentence"""
# import required libraris, json to work with API json format and requests to work with capturing payload data.
import requests, json

def emotion_detector(text_to_analyze):
    """ Function to run emotion analysis on submitted text captured under "text_to_analyze"""
    
    # URL Endpoint for the emotion analyzer
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers need for the emotion anlyzer to accept the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Capture the input into a object
    reqobj = { "raw_document": { "text": text_to_analyze }}

    # response oject containing the request made to the emotion analyzer. 
    response = requests.post(url, json = reqobj, headers = headers)
    #
    return response.text
