import pyttsx3

engine = pyttsx3.init()

print("Testing voice now...")
engine.say("Testing voice now")
engine.runAndWait()

command = input("Type hello: ")

if command == "hello":
    print("Speaking...")
    engine.say("Hello Rudraksh")
    engine.runAndWait()