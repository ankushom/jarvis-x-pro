import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import os

def send_message(event=None):

    text = entry.get()

    if text == "":
        return

    chat.insert(
        tk.END,
        "You: " + text + "\n"
    )

    chat.insert(
        tk.END,
        "Jarvis: V3 Dashboard Working\n\n"
    )

    entry.delete(0, tk.END)

def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

def open_calculator():
    os.system("calc")

root = tk.Tk()

root.title("JARVIS DASHBOARD V3")

root.geometry("1000x700")

button_frame = tk.Frame(root)

button_frame.pack(pady=10)

google_btn = tk.Button(
    button_frame,
    text="Google",
    command=open_google
)

google_btn.grid(
    row=0,
    column=0,
    padx=5
)

youtube_btn = tk.Button(
    button_frame,
    text="YouTube",
    command=open_youtube
)

youtube_btn.grid(
    row=0,
    column=1,
    padx=5
)

calc_btn = tk.Button(
    button_frame,
    text="Calculator",
    command=open_calculator
)

calc_btn.grid(
    row=0,
    column=2,
    padx=5
)

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

entry.bind(
    "<Return>",
    send_message
)

send_btn = tk.Button(
    root,
    text="Send",
    command=send_message
)

send_btn.pack()

root.mainloop()