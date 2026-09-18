"""
Jarvis X Pro
Custom Widgets
"""

import customtkinter as ctk
from datetime import datetime


class ChatBubble:

    def __init__(self, parent):

        self.parent = parent

        self.frame = ctk.CTkScrollableFrame(
            parent,
            fg_color="transparent"
        )

        self.frame.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=15
)
    def add_user(self, text):

        self._create_message(
            "👤 YOU",
            text,
            "#0A84FF"
        )

    def add_ai(self, text):

        self._create_message(
            "🤖 JARVIS",
            text,
            "#00C853"
        )

    def _create_message(self, sender, text, color):

        card = ctk.CTkFrame(
            self.frame,
            corner_radius=15
        )

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        header = ctk.CTkLabel(
            card,
            text=f"{sender}   {datetime.now().strftime('%H:%M')}",
            text_color=color,
            font=("Segoe UI", 14, "bold")
        )

        header.pack(
            anchor="w",
            padx=12,
            pady=(10, 5)
        )

        body = ctk.CTkLabel(
            card,
            text=text,
            justify="left",
            wraplength=650,
            font=("Segoe UI", 15)
        )

        body.pack(
            anchor="w",
            padx=12,
            pady=(0, 10)
        )