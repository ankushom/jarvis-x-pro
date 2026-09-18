"""
Jarvis X Pro
Desktop Automation Module
"""

import os
import subprocess
import pyautogui

pyautogui.FAILSAFE = True


def open_vscode():
    try:
        subprocess.Popen(["code"])
        return "Opening Visual Studio Code, Sir."
    except Exception:
        return "Sorry Sir, Visual Studio Code was not found in PATH."


def open_chrome():
    try:
        subprocess.Popen(["start", "chrome"], shell=True)
        return "Opening Google Chrome, Sir."
    except Exception:
        return "Sorry Sir, I couldn't open Google Chrome."


def open_downloads():
    try:
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads)
        return "Opening Downloads folder."
    except Exception:
        return "Sorry Sir, I couldn't open Downloads."


def create_folder(name):

    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        folder = os.path.join(desktop, name)

        os.makedirs(folder, exist_ok=True)

        return f"Folder '{name}' created successfully."

    except Exception as e:

        return f"Error: {e}"


def type_text(text):

    pyautogui.write(text, interval=0.03)

    return "Typing completed."


def press_enter():

    pyautogui.press("enter")

    return "Enter key pressed."


def minimize_window():

    pyautogui.hotkey("win", "down")

    return "Window minimized."


def maximize_window():

    pyautogui.hotkey("win", "up")

    return "Window maximized."


def copy():

    pyautogui.hotkey("ctrl", "c")

    return "Copied."


def paste():

    pyautogui.hotkey("ctrl", "v")

    return "Pasted."