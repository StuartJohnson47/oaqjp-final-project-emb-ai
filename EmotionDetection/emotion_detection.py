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
    
    # Fromatting the text vai json loads into a dictionary format.
    formatted_text = json.loads(response.text)
    
    # Pulling out the results from each emotion which is embedded in a dictionry/list/dictionary
    emotions = formatted_text['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    #Creating attributes and assinging default values for use in a for loop to find the highest value
    dominant_emotion = 'None'
    highest_score = 0

    ## for loop to go through the emotions.items and find the higest value and assign to the dominant_emotion attribute.
    for emotion, score in emotions.items():
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion

    ##Return results 
    return { 
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion}
        
