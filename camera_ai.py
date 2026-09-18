"""
Jarvis X Pro
AI Camera Vision Module
"""

import time
import cv2
from PIL import Image
from google import genai

from config import API_KEY

# Gemini Client
client = genai.Client(api_key=API_KEY)


def analyze_camera():
    """
    Capture one image from the webcam
    and analyze it using Gemini.
    """

    try:

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            return "Sorry Sir, I couldn't access the camera."

        print("Opening camera...")

        # Give the camera time to adjust exposure
        time.sleep(2)

        # Capture multiple frames so the image is clear
        ret = False
        frame = None

        for _ in range(10):
            ret, frame = cap.read()

        cap.release()

        if not ret:
            return "Sorry Sir, I couldn't capture an image."

        image_path = "camera_capture.jpg"

        cv2.imwrite(image_path, frame)

        image = Image.open(image_path)

        prompt = """
You are J.A.R.V.I.S. from Iron Man.

Analyze this camera image.

Rules:
- Reply in under 100 words.
- Begin with "Sir,".
- Describe what you can actually observe.
- Mention important objects.
- If a person is visible, describe only observable features such as clothing, posture, or actions. Do not identify them.
- Mention anything unusual.
- Be concise and natural.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                image
            ]
        )

        if response.text:
            return response.text.strip()

        return "Sorry Sir, I couldn't understand what the camera captured."

    except Exception as e:

        print("Camera Vision Error:", e)

        return f"Sorry Sir, an error occurred: {e}"