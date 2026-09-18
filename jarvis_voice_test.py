import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

while True:

    command = input("Enter Command: ")

    if command == "hello":
        speak("Hello Rudraksh")

    elif command == "exit":
        break