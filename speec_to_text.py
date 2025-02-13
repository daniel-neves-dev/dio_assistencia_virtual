import speech_recognition as sr
import webbrowser
import pyaudio
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")

        if "open youtube" in command:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            print("Opening Google...")
            webbrowser.open("https://www.google.com")
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")

recognize_speech()
