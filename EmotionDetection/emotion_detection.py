import json
import requests
def emotion_detector(text_to_analyze):
    #sent a request to watson nlp library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions']
    emotion_dict = emotions[0]['emotion']
    anger = emotion_dict['anger']
    disgust = emotion_dict['disgust']
    fear = emotion_dict['fear']
    joy = emotion_dict['joy']
    sadness = emotion_dict['sadness']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get) 
    output = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy':joy, 'sadness':sadness, 'dominant_emotion': dominant_emotion }
    return output


    