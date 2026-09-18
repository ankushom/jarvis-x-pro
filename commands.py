"""
Jarvis X Pro
Command Engine
"""

import webbrowser
import subprocess
import os


# ===============================
# WEB
# ===============================

def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_github():
    webbrowser.open("https://github.com")


def open_chatgpt():
    webbrowser.open("https://chat.openai.com")


# ===============================
# WINDOWS APPS
# ===============================

def open_notepad():
    subprocess.Popen("notepad.exe")


def open_calculator():
    subprocess.Popen("calc.exe")


def open_explorer():
    subprocess.Popen("explorer.exe")


def open_cmd():
    subprocess.Popen("cmd.exe")


def open_paint():
    subprocess.Popen("mspaint.exe")


def open_camera():
    os.system("start microsoft.windows.camera:")


# ===============================
# SYSTEM
# ===============================

def shutdown_pc():
    os.system("shutdown /s /t 1")


def restart_pc():
    os.system("shutdown /r /t 1")


def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")


# ===============================
# SCREENSHOT
# ===============================

def screenshot():

    from PIL import ImageGrab

    image = ImageGrab.grab()

    image.save("screenshot.png")

    return "screenshot.png"