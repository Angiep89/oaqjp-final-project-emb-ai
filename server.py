"""
Server module for the Emotion Detection application.
Provides routes to render the user interface and to analyze
text inputs for emotional content using Watson NLP.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Inicializar la aplicación Flask
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the provided text parameter for emotions and returns
    a formatted string output representing the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Validar si la emoción dominante es None (Manejo de Error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extraer variables con el formato limpio exigido
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application web interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    