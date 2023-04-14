from flask import Flask, request, jsonify
from .models.bird_call_recognizer import BirdCallRecognizer
from .utils.audio_processing import preprocess_audio

app = Flask(__name__)
recognizer = BirdCallRecognizer()

@app.route("/recognize", methods=["POST"])
def recognize_bird_call():
    audio_data = request.files["audio"]
    processed_audio = preprocess_audio(audio_data)
    results = recognizer.recognize(processed_audio)
    return jsonify(results)
