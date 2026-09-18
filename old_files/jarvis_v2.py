import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

speak("Jarvis Activated")

while True:
    command = input("Enter Command: ").lower()

    if command == "hello":
        speak("Hello Rudraksh")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif command == "exit":
        speak("Goodbye")
        break