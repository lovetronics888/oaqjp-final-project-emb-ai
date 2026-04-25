from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
#Flask instance
app = Flask(__name__)
@app.route("/emotionDetector")
def emot_detector():
    """
    Fetch text from requests,detect emotion and return formatted result
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."
    response = emotion_detector(text_to_analyze)
    formatted_output = (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
)


    return formatted_output

@app.route('/')
def render_index_page():
    """renders the home page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


