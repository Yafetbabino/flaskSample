""" Emotion detection """

import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    if (response.status_code ==400):
        formatted_output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_output


    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    # Determine the dominant emotion score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    dominant_emotion_score = emotion_scores[dominant_emotion]

    # Find the emotion name from the data
    for emotion, score in emotion_scores.items():
        if score == dominant_emotion_score:
            dominant_emotion_name = emotion
            break
        else: 
            return " Invalid text! Please try again!."

    formatted_output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion_name
        }
    return formatted_output
