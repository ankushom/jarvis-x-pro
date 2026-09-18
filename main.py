
import os
import datetime
import webbrowser
import pyttsx3
import pyautogui
from google import genai
from config import API_KEY

# ==========================
# GEMINI AI
# ==========================

client = genai.Client(
   api_key=API_KEY

)

# ==========================
# VOICE ENGINE
# ==========================

engine = pyttsx3.init()

voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)

    engine = pyttsx3.init()

    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    engine.say(str(text))
    engine.runAndWait()

    engine.stop()

# ==========================
# STARTUP
# ==========================

speak("Testing voice")
speak("Jarvis Activated")
speak("Welcome Rudraksh")

# ==========================
# MAIN LOOP
# ==========================

while True:

    command = input("\nEnter Command: ").lower()

    # TIME

    if "time" in command:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    # DATE

    elif "date" in command:

        today = datetime.date.today()
        speak(f"Today's date is {today}")

    # GOOGLE

    elif "google" in command:

        webbrowser.open("https://google.com")
        speak("Opening Google")

    # YOUTUBE

    elif "youtube" in command:

        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    # SEARCH

    elif "search" in command:

        query = input("What should I search? ")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        speak(f"Searching for {query}")

    # CHROME

    elif "chrome" in command:

        os.system("start chrome")
        speak("Opening Chrome")

    # NOTEPAD

    elif "notepad" in command:

        os.system("notepad")
        speak("Opening Notepad")

    # CALCULATOR

    elif "calculator" in command:

        os.system("calc")
        speak("Opening Calculator")

    # VS CODE

    elif "vscode" in command:

        os.system("code")
        speak("Opening Visual Studio Code")

    # SCREENSHOT

    elif "screenshot" in command:

        filename = (
            "screenshot_"
            + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".png"
        )

        image = pyautogui.screenshot()

        image.save(filename)

        speak("Screenshot saved successfully")

    # SAVE NOTE

    elif "note" in command:

        note = input("Write your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        speak("Note saved successfully")

    # TEST VOICE

    elif "test voice" in command:

        speak("Hello Rudraksh, voice is working perfectly")

    # AI CHAT

    elif "ai" in command:

        question = input("Ask AI: ")

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

            answer = response.text

            print("\nAI:", answer)

            speak(answer[:200])

        except Exception as e:

            print("AI Error:", e)

    # HELLO

    elif "hello" in command:

        speak("Hello Rudraksh, how can I help you")

    # WHO ARE YOU

    elif "who are you" in command:

        speak("I am Jarvis, your personal AI assistant")

    # HOW ARE YOU

    elif "how are you" in command:

        speak("I am fine and ready to help you")

    # EXIT

    elif "exit" in command:

        speak("Goodbye Rudraksh")
        break

    # UNKNOWN COMMAND

    else:

        speak("Sorry, I do not understand that command")

