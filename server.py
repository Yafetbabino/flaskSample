""" Emotion detector """

from flask import Flask, render_template, request
from Emotion.emotion import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """emotion alayzer"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print (f"For the given statement, the system response is {response} ")
    return f"For the given statement, the system response is 'anger': {response['anger']}, \
     'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, \
      and 'sadness':{response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """render the template """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
