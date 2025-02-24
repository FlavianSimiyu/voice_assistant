from flask import Flask, request, render_template
import openai
import speech_recognition as sr

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        if "audio" in request.files:
            audio_file = request.files["audio"]
            user_input = transcribe_audio(audio_file)
        else:
            user_input = request.form["user_input"]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        ai_response = response["choices"][0]["message"]["content"]
        return render_template("index.html", user_input=user_input, ai_response=ai_response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)