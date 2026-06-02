import requests
import json

def emotion_detector(text_to_analyze):
    # 1. Definición de la petición a la API (Igual que la Tarea 2)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # 2. Convertir la respuesta de texto plano a un diccionario de Python
    formatted_response = json.loads(response.text)
    
    # 3. Extraer el set de emociones específico del formato de Watson NLP
    # Estructura de Watson: formatted_response['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 4. Lógica para encontrar la emoción dominante (la que tenga el puntaje más alto)
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    
    # 5. Agregar la emoción dominante al diccionario final de salida
    emotion_dict['dominant_emotion'] = dominant_emotion
    
    return emotion_dict