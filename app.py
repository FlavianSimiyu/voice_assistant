import speech_recognition as sr
import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Could not request results. Check internet connection.")
        except sr.WaitTimeoutError:
            print("No speech detected. Try again.")
        return ""

def main():
    while True:
        command = input("Press Enter to start listening or type 'exit' to quit: ")
        if command.lower() == "exit":
            break
        
        user_input = listen()
        if user_input:
            response = f"You said: {user_input}. How can I assist you further?"
            print(response)
            threading.Thread(target=speak, args=(response,)).start()

if __name__ == "__main__":
    main()
