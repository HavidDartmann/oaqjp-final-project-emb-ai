"""
This is a Flask web application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotions():
    """
    Analyze the emotion of the text provided.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is not None:
        return result
    return "Invalid text! Please try again!"

if __name__ == '__main__':
    app.run(debug=True)
