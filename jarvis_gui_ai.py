from google import genai
import tkinter as tk
from tkinter import scrolledtext
from config import API_KEY


client = genai.Client(api_key=API_KEY)

def send_message():

    text = entry.get()

    if text == "":
        return

    chat.insert(tk.END, "You: " + text + "\n")

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text
        )

        answer = response.text

    except Exception as e:

        answer = "Error: " + str(e)

    chat.insert(tk.END, "Jarvis: " + answer + "\n\n")

    entry.delete(0, tk.END)

    chat.see(tk.END)

root = tk.Tk()

root.title("Jarvis AI Assistant")

root.geometry("900x650")

chat = scrolledtext.ScrolledText(
    root,
    width=100,
    height=30
)

chat.pack(pady=10)

entry = tk.Entry(
    root,
    width=80
)

entry.pack(pady=10)

button = tk.Button(
    root,
    text="Send",
    command=send_message
)

button.pack()

root.mainloop()