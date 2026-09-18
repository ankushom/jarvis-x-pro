"""
Jarvis X Pro
Controller Module
"""

import threading

from chatbot import ask_ai
from speech import speak

# Existing Commands
from commands import *
from automation import *
from media_control import *

# AI Vision
from screen_ai import capture_screen
from screen_vision import analyze_screen
from camera_ai import analyze_camera

# Modular Commands
from modules.browser import handle as browser_handle
from modules.desktop import handle as desktop_handle
from modules.media import handle as media_handle
from modules.vision import handle as vision_handle


class JarvisController:

    def __init__(self):
        self.status_callback = None

    def set_status_callback(self, callback):
        self.status_callback = callback

    def set_status(self, text, color):
        if self.status_callback:
            self.status_callback(text, color)

    def process(self, question: str):

        question = question.strip()

        if not question:
            return ""

        self.set_status(
            "🟡 THINKING...",
            "yellow"
        )

        cmd = question.lower()

        print("Command Received:", cmd)

        answer = None

        try:

            # =====================================
            # MODULAR COMMANDS
            # =====================================

            result = browser_handle(cmd)
            if result:
                answer = result

            if answer is None:
                result = desktop_handle(cmd)
                if result:
                    answer = result

            if answer is None:
                result = media_handle(cmd)
                if result:
                    answer = result

            if answer is None:
                result = vision_handle(cmd)
                if result:
                    answer = result

            # =====================================
            # REMAINING COMMANDS
            # =====================================

            if answer is None:
                                # ==================================
                # VS CODE
                # ==================================

                if (
                    "open vscode" in cmd
                    or "open visual studio code" in cmd
                ):

                    answer = open_vscode()

                # ==================================
                # FILE EXPLORER
                # ==================================

                elif (
                    "open explorer" in cmd
                    or "open file explorer" in cmd
                ):

                    open_explorer()
                    answer = "Opening File Explorer."

                # ==================================
                # DOWNLOADS
                # ==================================

                elif "open downloads" in cmd:

                    answer = open_downloads()

                # ==================================
                # CMD
                # ==================================

                elif (
                    "open cmd" in cmd
                    or "open command prompt" in cmd
                ):

                    open_cmd()
                    answer = "Opening Command Prompt."

                # ==================================
                # PAINT
                # ==================================

                elif "open paint" in cmd:

                    open_paint()
                    answer = "Opening Paint."

                # ==================================
                # CAMERA
                # ==================================

                elif "open camera" in cmd:

                    open_camera()
                    answer = "Opening Camera."

                # ==================================
                # SCREENSHOT
                # ==================================

                elif (
                    "take screenshot" in cmd
                    or "capture screenshot" in cmd
                ):

                    path = screenshot()
                    answer = f"Screenshot saved successfully at {path}"

                # ==================================
                # AI SCREEN VISION
                # ==================================

                elif (
                    "analyze screen" in cmd
                    or "analyze my screen" in cmd
                    or "what is on my screen" in cmd
                    or "screen vision" in cmd
                ):

                    print(">>> SCREEN COMMAND DETECTED <<<")

                    path = capture_screen()
                    answer = analyze_screen(path)

                # ==================================
                # AI CAMERA VISION
                # ==================================

                elif (
                    "what do you see" in cmd
                    or "what can you see" in cmd
                    or "look around" in cmd
                    or "look at me" in cmd
                    or "camera vision" in cmd
                    or "analyze camera" in cmd
                ):

                    print(">>> CAMERA COMMAND DETECTED <<<")

                    answer = analyze_camera()

                # ==================================
                # CREATE FOLDER
                # ==================================

                elif cmd.startswith("create folder"):

                    folder_name = (
                        question.replace("Create folder", "")
                        .replace("create folder", "")
                        .strip()
                    )

                    if not folder_name:
                        folder_name = "New Folder"

                    answer = create_folder(folder_name)

                # ==================================
                # TYPE TEXT
                # ==================================

                elif cmd.startswith("type "):

                    text = question[5:]
                    answer = type_text(text)

                # ==================================
                # PRESS ENTER
                # ==================================

                elif "press enter" in cmd:

                    answer = press_enter()

                # ==================================
                # COPY
                # ==================================

                elif cmd == "copy":

                    answer = copy()

                # ==================================
                # PASTE
                # ==================================

                elif cmd == "paste":

                    answer = paste()

                # ==================================
                # MINIMIZE WINDOW
                # ==================================

                elif (
                    "minimize window" in cmd
                    or "minimize this window" in cmd
                ):

                    answer = minimize_window()

                # ==================================
                # MAXIMIZE WINDOW
                # ==================================

                elif (
                    "maximize window" in cmd
                    or "maximize this window" in cmd
                ):

                    answer = maximize_window()

                # ==================================
                # AI CHAT (DEFAULT)
                # ==================================

                else:

                    answer = ask_ai(question)
        except Exception as e:

            print("Controller Error:", e)

            answer = f"An error occurred: {e}"

        # ==================================
        # SPEAK RESPONSE
        # ==================================

        self.set_status(
            "🔊 SPEAKING...",
            "#00bfff"
        )

        def speak_and_reset():

            try:
                speak(answer)

            except Exception as e:
                print("Speech Error:", e)

            self.set_status(
                "🟢 AI ONLINE",
                "#00ff88"
            )

        threading.Thread(
            target=speak_and_reset,
            daemon=True
        ).start()

        return answer