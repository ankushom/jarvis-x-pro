import customtkinter as ctk
import tkinter as tk
import threading
import socket
import psutil

from datetime import datetime

from listener import listen

from controller import JarvisController

# ==========================================
# APP SETTINGS
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_NAME = "JARVIS X PRO"

BG = "#1e1e1e"
PANEL = "#2b2b2b"
ACCENT = "#00d4ff"

# ==========================================
# APP
# ==========================================

app = ctk.CTk()

app.title(APP_NAME)

app.geometry("1600x950")

app.minsize(1400, 850)

app.configure(fg_color=BG)


controller = JarvisController()
# ==========================================
# HEADER
# ==========================================

header = ctk.CTkFrame(
    app,
    fg_color=PANEL,
    height=120,
    corner_radius=20
)

header.pack(
    fill="x",
    padx=15,
    pady=15
)

title = ctk.CTkLabel(
    header,
    text="⚡ JARVIS X PRO ⚡",
    font=("Segoe UI", 40, "bold"),
    text_color=ACCENT
)

title.pack(
    pady=(15, 5)
)

clock = ctk.CTkLabel(
    header,
    text="",
    font=("Consolas", 26, "bold"),
    text_color="#00ffff"
)

clock.pack(
    pady=(0, 15)
)

# ==========================================
# LIVE CLOCK
# ==========================================

def update_clock():

    clock.configure(
        text=datetime.now().strftime("%H:%M:%S")
    )

    app.after(
        1000,
        update_clock
    )

update_clock()

# ==========================================
# CHAT FUNCTION
# ==========================================

def add_chat(sender, message):

    current = datetime.now().strftime("%H:%M")

    if sender == "user":

        chat_box.insert(
            "end",
            f"\n👤 YOU  ",
            "user"
        )

    else:

        chat_box.insert(
            "end",
            f"\n🤖 JARVIS  ",
            "jarvis"
        )

    chat_box.insert(
        "end",
        f"[{current}]\n",
        "time"
    )

    chat_box.insert(
        "end",
        message + "\n\n",
        "message"
    )

    chat_box.see("end")



# ==========================================
# SEND MESSAGE
# ==========================================

def send_message():

    question = entry.get().strip()

    if not question:
        return

    chat_box.insert(
        "end",
        f"👤 You:\n{question}\n\n"
    )

    chat_box.see("end")

    entry.delete(0, "end")

    answer = controller.process(question)

    add_chat(
    "jarvis",
    answer
)

def update_ai_status(text, color):

    ai.configure(
        text=text,
        text_color=color
    )

controller.set_status_callback(update_ai_status)


# ==========================================
# MIC
# ==========================================

def start_listening():

    ai.configure(
        text="🎤 LISTENING...",
        text_color="cyan"
    )

    try:

        text = listen()

        if text.strip():

            entry.delete(0, "end")
            entry.insert(0, text)

            send_message()

    except Exception as e:

        print(e)

    ai.configure(
        text="🟢 AI ONLINE",
        text_color="#00ff88"
    )


# ==========================================
# SYSTEM
# ==========================================

def update_system():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    cpu_label.configure(
        text=f"🖥 CPU : {cpu}%"
    )

    ram_label.configure(
        text=f"🧠 RAM : {ram}%"
    )

    try:

        battery = psutil.sensors_battery()

        if battery:

            battery_label.configure(
                text=f"🔋 Battery : {battery.percent:.0f}%"
            )

    except:
        pass

    try:

        socket.create_connection(
            ("8.8.8.8",53),
            timeout=2
        )

        internet_label.configure(
            text="🌐 Internet : Connected",
            text_color="#00ff88"
        )

    except:

        internet_label.configure(
            text="🌐 Internet : Offline",
            text_color="red"
        )

    app.after(
        1000,
        update_system
    )

# ==========================================
# MAIN FRAME
# ==========================================

main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

main_frame.grid_columnconfigure(
    0,
    weight=1
)

main_frame.grid_columnconfigure(
    1,
    weight=3
)

main_frame.grid_columnconfigure(
    2,
    weight=1
)

main_frame.grid_rowconfigure(
    0,
    weight=1
)

# ==========================================
# LEFT PANEL
# ==========================================

left_panel = ctk.CTkFrame(
    main_frame,
    fg_color=PANEL,
    corner_radius=20
)

left_panel.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=(0, 10)
)

left_title = ctk.CTkLabel(
    left_panel,
    text="⚡ COMMAND CENTER",
    font=("Segoe UI", 22, "bold"),
    text_color=ACCENT
)

left_title.pack(pady=20)

buttons = [
    "🌐 Google",
    "📺 YouTube",
    "🧮 Calculator",
    "📝 Notepad",
    "📂 Explorer",
    "💻 CMD",
    "⚙ Settings"
]

for name in buttons:

    btn = ctk.CTkButton(
        left_panel,
        text=name,
        width=220,
        height=45,
        corner_radius=12
    )

    btn.pack(
        pady=8,
        padx=15
    )

# ==========================================
# CENTER PANEL
# ==========================================

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

center_panel.grid_rowconfigure(0, weight=0)
center_panel.grid_rowconfigure(1, weight=0)
center_panel.grid_rowconfigure(2, weight=1)
center_panel.grid_rowconfigure(3, weight=0)

center_panel.grid_columnconfigure(0, weight=1)

center_title = ctk.CTkLabel(
    center_panel,
    text="⚡ JARVIS CORE ⚡",
    font=("Segoe UI", 28, "bold"),
    text_color=ACCENT
)

center_title.grid(
    row=0,
    column=0,
    pady=20
)

# ==========================================
# REACTOR
# ==========================================

reactor = tk.Canvas(
    center_panel,
    width=300,
    height=300,
    bg=PANEL,
    highlightthickness=0
)

reactor.grid(
    row=1,
    column=0,
    pady=10
)

reactor.create_oval(
    20,
    20,
    280,
    280,
    outline="#00ffff",
    width=4
)

reactor.create_oval(
    60,
    60,
    240,
    240,
    outline="#00bfff",
    width=3
)

reactor.create_oval(
    120,
    120,
    180,
    180,
    fill="#00ffff",
    outline="#00ffff"
)

reactor.create_text(
    150,
    150,
    text="AI",
    fill="black",
    font=("Segoe UI", 16, "bold")
)

# ==========================================
# CHAT
# ==========================================

chat_box = tk.Text()

# ==========================================
# RIGHT PANEL
# ==========================================

right_panel = ctk.CTkFrame(
    main_frame,
    fg_color=PANEL,
    corner_radius=20
)

right_panel.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=(10, 0)
)

status = ctk.CTkLabel(
    right_panel,
    text="⚡ SYSTEM STATUS",
    font=("Segoe UI", 22, "bold"),
    text_color=ACCENT
)

status.pack(pady=20)

cpu_label = ctk.CTkLabel(
    right_panel,
    text="🖥 CPU : 0%",
    font=("Segoe UI", 16)
)

cpu_label.pack(pady=12)

ram_label = ctk.CTkLabel(
    right_panel,
    text="🧠 RAM : 0%",
    font=("Segoe UI", 16)
)

ram_label.pack(pady=12)

battery_label = ctk.CTkLabel(
    right_panel,
    text="🔋 Battery : --%",
    font=("Segoe UI", 16)
)

battery_label.pack(pady=12)

internet_label = ctk.CTkLabel(
    right_panel,
    text="🌐 Internet : Checking...",
    font=("Segoe UI", 16)
)

internet_label.pack(pady=12)

ai = ctk.CTkLabel(
    right_panel,
    text="🟢 AI ONLINE",
    font=("Segoe UI", 18, "bold"),
    text_color="#00ff88"
)

ai.pack(pady=20)

# ==========================================
# INPUT AREA
# ==========================================

input_frame = ctk.CTkFrame(
    center_panel,
    fg_color="transparent"
)

input_frame.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=20,
    pady=(0,20)
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
    height=50,
    corner_radius=15,
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
    width=55,
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
    lambda e: send_message()
)

update_system()

app.mainloop()