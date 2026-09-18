"""
Jarvis X Pro
Animations Module
"""

import math


class ReactorAnimation:

    def __init__(self, canvas, rings):

        self.canvas = canvas
        self.rings = rings

        self.angle = 0

        self.speed = 2

        self.running = True

    def set_speed(self, speed):

        self.speed = speed

    def animate(self):

        if not self.running:
            return

        self.angle += self.speed

        for i, ring in enumerate(self.rings):

            start = self.angle + (i * 45)

            self.canvas.itemconfigure(
                ring,
                start=start
            )

        self.canvas.after(
            30,
            self.animate
        )