"""
Jarvis X Pro
AI Screen Vision Module
"""

from google import genai
from PIL import Image

from config import API_KEY

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)


def analyze_screen(image_path):
    """
    Analyze a screenshot using Gemini Vision.
    """

    try:

        image = Image.open(image_path)

        prompt = """
You are J.A.R.V.I.S. (Just A Rather Very Intelligent System) from Iron Man.

Analyze the screenshot and reply naturally like Jarvis.

Rules:
- Keep your response under 120 words.
- Be professional and concise.
- Start with "Sir," or "Greetings, Sir,".
- Mention:
  1. Which application or website is open.
  2. What the user appears to be doing.
  3. Any visible errors, warnings, or important observations.
  4. If code is visible, explain the issue briefly and suggest a fix.
  5. If no problems are found, simply state that everything appears normal.

Do not describe every small UI element.
Do not repeat unnecessary details.
Speak like a real AI assistant.
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

        return "Sorry Sir, I couldn't understand the current screen."

    except Exception as e:

        print("Screen Vision Error:", e)

        return (
            "Sorry Sir, I encountered an error while analyzing your screen."
        )