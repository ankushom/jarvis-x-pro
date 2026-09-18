import customtkinter as ctk
from datetime import datetime
from animations import ReactorAnimation
from listener import listen
from chatbot import ask_ai
from speech import speak

from chatbot import ask_ai
from listener import listen
from speech import speak
from commands import *

import psutil
import threading
import socket

# -----------------------------
# APP SETTINGS
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("JARVIS X PRO")
app.geometry("1600x950")
app.minsize(1400, 850)

# -----------------------------
# COLORS
# -----------------------------
BG = "#1e1e1e"
PANEL = "#2b2b2b"
ACCENT = "#00d4ff"

app.configure(fg_color=BG)

# -----------------------------
# HEADER
# -----------------------------
header = ctk.CTkFrame(
    app,
    fg_color=PANEL,
    corner_radius=20,
    height=120
)

header.pack(
    fill="x",
    padx=15,
    pady=15
)

title = ctk.CTkLabel(
    header,
    text="⚡ JARVIS X PRO ⚡",
    font=("Segoe UI", 42, "bold"),
    text_color=ACCENT
)

title.pack(
    pady=(15, 0)
)

clock = ctk.CTkLabel(
    header,
    text="",
    font=("Consolas", 28, "bold"),
    text_color="#00ffff"
)

clock.pack(
    pady=(5, 15)
)

# -----------------------------
# LIVE CLOCK
# -----------------------------
def update_clock():
    clock.configure(
        text=datetime.now().strftime("%H:%M:%S")
    )
    app.after(1000, update_clock)

update_clock()

# =====================================
# MAIN CONTAINER
# =====================================

main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0,15)
)

# GRID CONFIGURATION
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=3)
main_frame.grid_columnconfigure(2, weight=1)

main_frame.grid_rowconfigure(0, weight=1)


# =====================================
# LEFT PANEL
# =====================================

left_panel = ctk.CTkFrame(
    main_frame,
    fg_color=PANEL,
    corner_radius=20
)

left_panel.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=(0,10)
)

left_title = ctk.CTkLabel(
    left_panel,
    text="⚡ COMMAND CENTER",
    font=("Segoe UI",22,"bold"),
    text_color=ACCENT
)

left_title.pack(
    pady=20
)

buttons = [
    "🌐 Google",
    "📺 YouTube",
    "🧮 Calculator",
    "📝 Notepad",
    "📂 Explorer",
    "🌦 Weather",
    "⚙ Settings"
]

for item in buttons:

    ctk.CTkButton(
        left_panel,
        text=item,
        width=220,
        height=45,
        corner_radius=10
    ).pack(
        pady=8,
        padx=15
    )


# =====================================
# CENTER PANEL
# =====================================

center_panel = ctk.CTkFrame(
    main_frame,
    fg_color=PANEL,
    corner_radius=20
)

center_panel.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10
)

center_title = ctk.CTkLabel(
    center_panel,
    text="⚡ JARVIS CORE ⚡",
    font=("Segoe UI",30,"bold"),
    text_color=ACCENT
)

center_title.grid(
    row=0,
    column=0,
    pady=20
)

# =====================================
# CENTER PANEL GRID
# =====================================

center_panel.grid_rowconfigure(0, weight=0)   # Title
center_panel.grid_rowconfigure(1, weight=0)   # Reactor
center_panel.grid_rowconfigure(2, weight=1)   # Chat (expand)
center_panel.grid_rowconfigure(3, weight=0)   # Input Bar

center_panel.grid_columnconfigure(0, weight=1)

import tkinter as tk

reactor = tk.Canvas(
    center_panel,
    width=320,
    height=320,
    bg=PANEL,
    highlightthickness=0
)

reactor.grid(
    row=1,
    column=0,
    pady=20
)

import math

rings2 = []

for i in range(8):

    arc = reactor.create_arc(
        55,
        55,
        265,
        265,
        start=i * 45,
        extent=22,
        style="arc",
        outline="#00bfff",
        width=3
    )

    rings2.append(arc)

    rings3 = []

for i in range(4):

    arc = reactor.create_arc(
        95,
        95,
        225,
        225,
        start=i * 90,
        extent=40,
        style="arc",
        outline="#66ffff",
        width=5
    )

    rings3.append(arc)

center = reactor.create_oval(
    120,
    120,
    200,
    200,
    fill="#00E5FF",
    outline="#00FFFF",
    width=2
)

text = reactor.create_text(
    160,
    160,
    text="AI\nONLINE",
    fill="black",
    font=("Segoe UI",16,"bold"),
    justify="center"
)

chat_box = ctk.CTkTextbox(
    center_panel,
    width=780,
    height=250,
    corner_radius=15,
    border_width=2,
    border_color=ACCENT,
    font=("Segoe UI",16)
)

chat_box.grid(
    row=2,
    column=0,
    padx=20,
    pady=15,
    sticky="nsew"
)

chat_box.insert(
    "end",
    "⚡ Jarvis X Pro Online\n\n"
)

# =====================================
# INPUT AREA
# =====================================

input_frame = ctk.CTkFrame(
    center_panel,
    fg_color="transparent"
)

input_frame.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=20,
    pady=20
)

input_frame.grid_columnconfigure(0, weight=1)

entry = ctk.CTkEntry(
    input_frame,
    height=50,
    corner_radius=15,
    border_width=2,
    border_color=ACCENT,
    placeholder_text="⚡ Ask Jarvis Anything..."
)

entry.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=(0,10)
)

mic_btn = ctk.CTkButton(
    input_frame,
    text="🎤",
    width=55,
    command=lambda: threading.Thread(
        target=start_listening,
        daemon=True
    ).start()
)

mic_btn.grid(
    row=0,
    column=1,
    padx=5
)

send_btn = ctk.CTkButton(
    input_frame,
    text="➜",
    width=50,
    height=50,
    corner_radius=15,
    command=send_message
)

send_btn.grid(
    row=0,
    column=2
)

entry.bind(
    "<Return>",
    lambda event: send_message()
)

# =====================================
# RIGHT PANEL
# =====================================

right_panel = ctk.CTkFrame(
    main_frame,
    fg_color=PANEL,
    corner_radius=20
)

right_panel.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=(10,0)
)

status = ctk.CTkLabel(
    right_panel,
    text="⚡ SYSTEM STATUS",
    font=("Segoe UI",22,"bold"),
    text_color=ACCENT
)

status.pack(
    pady=20
)

cpu_label = ctk.CTkLabel(
    right_panel,
    text="CPU : 0%",
    font=("Segoe UI",16)
)

cpu_label.pack(pady=15)


ram_label = ctk.CTkLabel(
    right_panel,
    text="RAM : 0%",
    font=("Segoe UI",16)
)

ram_label.pack(pady=15)

battery_label = ctk.CTkLabel(
    right_panel,
    text="Battery : --%",
    font=("Segoe UI",16)
)

battery_label.pack(pady=15)

internet_label = ctk.CTkLabel(
    right_panel,
    text="Internet : Checking...",
    font=("Segoe UI",16)
)

internet_label.pack(pady=15)


ai = ctk.CTkLabel(
    right_panel,
    text="🟢 AI ONLINE",
    text_color="#00ff88",
    font=("Segoe UI",18,"bold")
)

ai.pack(
    pady=20
)

def send_message():

    question = entry.get().strip()

    if not question:
        return

    chat_box.insert("end", f"👤 You:\n{question}\n\n")
    chat_box.see("end")

    entry.delete(0, "end")

    ai.configure(
        text="🟡 THINKING...",
        text_color="yellow"
    )

    cmd = question.lower()

    try:

        # ---------- COMMANDS ----------

        if "open google" in cmd:
            open_google()
            answer = "Opening Google."

        elif "open youtube" in cmd:
            open_youtube()
            answer = "Opening YouTube."

        elif "open github" in cmd:
            open_github()
            answer = "Opening GitHub."

        elif "open chatgpt" in cmd:
            open_chatgpt()
            answer = "Opening ChatGPT."

        elif "open calculator" in cmd:
            open_calculator()
            answer = "Opening Calculator."

        elif "open notepad" in cmd:
            open_notepad()
            answer = "Opening Notepad."

        elif "open explorer" in cmd:
            open_explorer()
            answer = "Opening File Explorer."

        elif "open cmd" in cmd:
            open_cmd()
            answer = "Opening Command Prompt."

        else:
            answer = ask_ai(question)

    except Exception as e:

        print(e)
        answer = "Sorry Boss, something went wrong."

    chat_box.insert(
        "end",
        f"🤖 Jarvis:\n{answer}\n\n"
    )

    chat_box.see("end")

    ai.configure(
        text="🟢 SPEAKING...",
        text_color="#00ff88"
    )

    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()

    ai.configure(
        text="🟢 AI ONLINE",
        text_color="#00ff88"
    )


def update_system():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    cpu_label.configure(text=f"CPU : {cpu}%")
    ram_label.configure(text=f"RAM : {ram}%")

    try:
        battery = psutil.sensors_battery()

        if battery:
            battery_label.configure(
                text=f"Battery : {battery.percent:.0f}%"
            )
        else:
            battery_label.configure(text="Battery : N/A")

    except:
        battery_label.configure(text="Battery : N/A")

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)

        internet_label.configure(
            text="Internet : Connected",
            text_color="#00ff88"
        )

    except:
        internet_label.configure(
            text="Internet : Offline",
            text_color="red"
        )

    app.after(1000, update_system)


# Start Updating
update_system()

# Start GUI
app.mainloop()