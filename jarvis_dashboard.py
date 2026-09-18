from google import genai
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import os
from config import API_KEY


client = genai.Client(
    api_key=API_KEY
)

def send_message():

    text = entry.get()

    if text == "":
        return

    chat.insert(
        tk.END,
        "You: " + text + "\n"
    )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text
        )

        answer = response.text

    except Exception as e:

        answer = str(e)

    chat.insert(
        tk.END,
        "Jarvis: " + answer + "\n\n"
    )

    entry.delete(0, tk.END)

def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

root = tk.Tk()

root.title("Jarvis Dashboard")

root.geometry("1000x700")

chat = scrolledtext.ScrolledText(
    root,
    width=120,
    height=30
)

chat.pack(pady=10)

entry = tk.Entry(
    root,
    width=80
)

entry.pack(pady=10)

send_btn = tk.Button(
    root,
    text="Send",
    command=send_message
)

send_btn.pack()

google_btn = tk.Button(
    root,
    text="Google",
    command=open_google
)

google_btn.pack()

youtube_btn = tk.Button(
    root,
    text="YouTube",
    command=open_youtube
)

youtube_btn.pack()

root.mainloop()