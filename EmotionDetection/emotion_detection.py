import requests
import json

def emotion_detector(text_to_analyze):
    # Step 1: Handle blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    # Step 2: Send request to API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    # Step 3: Parse API response
    response_dict = json.loads(response.text)

    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Step 4: Extract scores
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Step 5: Identify dominant emotion
    dominant = max(emotions, key=emotions.get)

    # Step 6: Return final result
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant,
        'status_code': 200
    }
