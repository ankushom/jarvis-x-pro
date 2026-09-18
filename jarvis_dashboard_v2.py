from listener import listen
import threading
from chatbot import ask_ai
import customtkinter as ctk
import tkinter as tk
import webbrowser
import os
import subprocess
from datetime import datetime

import pyttsx3
import psutil

# ==========================
# VOICE ENGINE
# ==========================

engine = pyttsx3.init()

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

def speak(text):
    try:
        engine.say(str(text))
        engine.runAndWait()
    except:
        pass

# ==========================
# COMMANDS
# ==========================

def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_explorer():
    os.startfile("C:\\")

def open_chrome():
    try:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(chrome_path)
    except:
        webbrowser.open("https://google.com")

# ==========================
# WINDOW
# ==========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("JARVIS X V3")
root.geometry("1600x950")

# ==========================
# HEADER
# ==========================

header = ctk.CTkFrame(
    root,
    corner_radius=20
)

header.pack(
    fill="x",
    padx=15,
    pady=10
)

title = ctk.CTkLabel(
    header,
    text="⚡ JARVIS X ⚡",
    font=("Arial", 42, "bold"),
    text_color="#00d4ff"
)

title.pack(
    pady=10
)

clock_label = ctk.CTkLabel(
    header,
    text="",
    font=("Consolas", 30, "bold"),
    text_color="#00ffff"
)

clock_label.pack(
    pady=5
)

def update_clock():

    current_time = datetime.now().strftime("%H:%M:%S")

    clock_label.configure(
        text=current_time
    )

    root.after(
        1000,
        update_clock
    )

update_clock()

# ==========================
# MAIN FRAME
# ==========================

main_frame = ctk.CTkFrame(
    root,
    corner_radius=20
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# ==========================
# LEFT SIDEBAR
# ==========================

sidebar = ctk.CTkFrame(
    main_frame,
    width=250,
    corner_radius=20
)

sidebar.pack(
    side="left",
    fill="y",
    padx=10,
    pady=10
)

ctk.CTkLabel(
    sidebar,
    text="⚡ COMMAND CENTER ⚡",
    font=("Arial", 22, "bold"),
    text_color="#00d4ff"
).pack(
    pady=20
)

# BUTTONS

ctk.CTkButton(
    sidebar,
    text="🌐 GOOGLE",
    command=open_google
).pack(
    pady=8,
    padx=10,
    fill="x"
)

ctk.CTkButton(
    sidebar,
    text="📺 YOUTUBE",
    command=open_youtube
).pack(
    pady=8,
    padx=10,
    fill="x"
)

ctk.CTkButton(
    sidebar,
    text="🧮 CALCULATOR",
    command=open_calculator
).pack(
    pady=8,
    padx=10,
    fill="x"
)

ctk.CTkButton(
    sidebar,
    text="📝 NOTEPAD",
    command=open_notepad
).pack(
    pady=8,
    padx=10,
    fill="x"
)

ctk.CTkButton(
    sidebar,
    text="📂 EXPLORER",
    command=open_explorer
).pack(
    pady=8,
    padx=10,
    fill="x"
)

ctk.CTkButton(
    sidebar,
    text="🌐 CHROME",
    command=open_chrome
).pack(
    pady=8,
    padx=10,
    fill="x"
)

# ==========================
# CENTER PANEL
# ==========================

center = ctk.CTkFrame(
    main_frame,
    corner_radius=20
)

center.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

core_label = ctk.CTkLabel(
    center,
    text="⚡ JARVIS CORE ONLINE ⚡",
    font=("Arial", 30, "bold"),
    text_color="#00d4ff"
)

core_label.pack(
    pady=20
)

# ==========================
# ARC REACTOR
# ==========================

reactor_canvas = tk.Canvas(
    center,
    width=280,
    height=200,
    bg="#2b2b2b",
    highlightthickness=0
)

reactor_canvas.pack(
    pady=10
)

outer_ring = reactor_canvas.create_oval(
    10, 10, 210, 210,
    outline="#00ffff",
    width=5
)

middle_ring = reactor_canvas.create_oval(
    30, 30, 190, 190,
    outline="#00d4ff",
    width=4
)

inner_ring = reactor_canvas.create_oval(
    70, 70, 150, 150,
    fill="#00ffff",
    outline="#00ffff"
)

reactor_text = reactor_canvas.create_text(
    110,
    110,
    text="JARVIS",
    fill="black",
    font=("Arial", 12, "bold")
)


# ==========================
# CHAT AREA
# ==========================

chat_box = ctk.CTkTextbox(
    center,
    width=850,
    height=180,
    corner_radius=15,
    border_width=2,
    border_color="#00d4ff"
)

chat_box.pack(
    padx=20,
    pady=10
)

entry = ctk.CTkEntry(
    center,
    width=850,
    height=50,
    corner_radius=15,
    border_width=2,
    border_color="#00d4ff",
    placeholder_text="⚡ Ask Jarvis Anything..."
)

entry.pack(
    pady=10
)

# ==========================
# RIGHT STATUS PANEL
# ==========================

status_panel = ctk.CTkFrame(
    main_frame,
    width=280,
    corner_radius=20
)

status_panel.pack(
    side="right",
    fill="y",
    padx=10,
    pady=10
)
status_panel.pack_propagate(False)

ctk.CTkLabel(
    status_panel,
    text="⚡ SYSTEM STATUS ⚡",
    font=("Arial", 22, "bold"),
    text_color="#00d4ff"
).pack(
    pady=20
)

cpu_label = ctk.CTkLabel(
    status_panel,
    text="CPU : 0%"
)

cpu_label.pack(
    pady=10
)

ram_label = ctk.CTkLabel(
    status_panel,
    text="RAM : 0%"
)

ram_label.pack(
    pady=10
)

battery_label = ctk.CTkLabel(
    status_panel,
    text="Battery : --%"
)

battery_label.pack(
    pady=10
)

ai_status_label = ctk.CTkLabel(
    status_panel,
    text="🟢 AI ONLINE",
    font=("Arial", 18, "bold"),
    text_color="#00ff88"
)

ai_status_label.pack(
    pady=10
)

# ==========================
# SEND MESSAGE
# ==========================


def start_listening():

    try:
        ai_status_label.configure(
            text="🎤 LISTENING...",
            text_color="cyan"
        )

        text = listen()

        if text.strip():

            entry.delete(0, "end")
            entry.insert(0, text)

            send_message()

    except Exception as e:
        print(e)

    finally:

        ai_status_label.configure(
            text="🟢 AI ONLINE",
            text_color="#00ff88"
        )


def send_message():

    text = entry.get()

    ai_status_label.configure(
        text="🟡 THINKING",
        text_color="yellow"
    )

    if text.strip() == "":
        return

    text_lower = text.lower()

    if text_lower == "hello":

        answer = "Hello Boss! Jarvis Online."

    elif text_lower == "time":

        answer = datetime.now().strftime("%H:%M:%S")

    elif text_lower == "date":

        answer = datetime.now().strftime("%d-%m-%Y")

    elif text_lower == "open google":

        open_google()
        answer = "Opening Google"

    elif text_lower == "open youtube":

        open_youtube()
        answer = "Opening YouTube"

    elif text_lower == "open calculator":

        open_calculator()
        answer = "Opening Calculator"

    elif text_lower == "open notepad":

        open_notepad()
        answer = "Opening Notepad"

    elif text_lower == "open explorer":

        open_explorer()
        answer = "Opening Explorer"

    elif text_lower == "open chrome":

        open_chrome()
        answer = "Opening Chrome"

    elif text_lower == "system":

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        answer = f"CPU {cpu}% | RAM {ram}%"

    else:

        try:

            ai_status_label.configure(
                text="🟡 AI THINKING...",
                text_color="yellow"
            )

            answer = ask_ai(text)

        except Exception as e:

            print("AI Error:", e)

            answer = "Sorry Boss, AI is not responding."

    chat_box.insert(
        "end",
        "🤖 Jarvis: " + answer + "\n\n"
    )

    chat_box.see("end")

    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()

    ai_status_label.configure(
        text="🟢 AI ONLINE",
        text_color="#00ff88"
    )

    entry.delete(
        0,
        "end"
    )

# ==========================
# SEND BUTTON
# ==========================

send_btn = ctk.CTkButton(
    center,
    text="🚀 SEND",
    width=220,
    height=50,
    command=send_message
)

send_btn.pack(
    pady=10
)

mic_btn = ctk.CTkButton(
    center,
    text="🎤 MIC",
    width=220,
    height=50,
    command=lambda: threading.Thread(
        target=start_listening,
        daemon=True
    ).start()
)

mic_btn.pack(
    side="top",
    pady=20
)


entry.bind(
    "<Return>",
    lambda event: send_message()
)

# ==========================
# SYSTEM MONITOR
# ==========================

def update_system():

    try:

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        cpu_label.configure(
            text=f"CPU : {cpu}%"
        )

        ram_label.configure(
            text=f"RAM : {ram}%"
        )

        battery = psutil.sensors_battery()

        if battery:

            battery_label.configure(
                text=f"Battery : {battery.percent}%"
                
            )

    except:
        pass

    root.after(
        1000,
        update_system
    )

update_system()

# ==========================
# ARC REACTOR ANIMATION
# ==========================

glow_state = 0

def animate_reactor():

    global glow_state

    if glow_state == 0:

        reactor_canvas.itemconfig(
            outer_ring,
            outline="#00ffff"
        )

        reactor_canvas.itemconfig(
            middle_ring,
            outline="#00d4ff"
        )

        glow_state = 1

    else:

        reactor_canvas.itemconfig(
            outer_ring,
            outline="#00d4ff"
        )

        reactor_canvas.itemconfig(
            middle_ring,
            outline="#00ffff"
        )

        glow_state = 0

    root.after(
        400,
        animate_reactor
    )

animate_reactor()


# ==========================
# STARTUP MESSAGE
# ==========================

speak("Welcome Back Boss. Jarvis Online.")

chat_box.insert(
    "end",
    "⚡ JARVIS X ONLINE ⚡\n\n"
)

chat_box.insert(
    "end",
    "Type HELLO, TIME, DATE or SYSTEM.\n\n"
)

# ==========================
# RUN APP
# ==========================

footer = ctk.CTkFrame(
    root,
    height=40,
    corner_radius=0
)

footer.pack(
    fill="x",
    side="bottom"
)

footer_label = ctk.CTkLabel(
    footer,
    text="⚡ JARVIS X | AI CORE ONLINE | Developed By Ankush ⚡",
    font=("Arial", 14, "bold"),
    text_color="#00d4ff"
)

footer_label.pack(
    pady=5
)

root.mainloop()