import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

while True:
    command = input("Enter Command: ").lower()

    if command == "hello":
        speak("Hello Rudraksh")

    elif command == "test":
        speak("Voice test successful")

    elif command == "exit":
        speak("Goodbye")
        break