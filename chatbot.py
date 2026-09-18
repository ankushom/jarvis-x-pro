from google import genai
from config import API_KEY, SYSTEM_PROMPT
from memory import add_history, get_history

client = genai.Client(api_key=API_KEY)


def ask_ai(prompt: str):

    if not prompt.strip():
        return ""

    try:

        history = get_history()

        memory_context = ""

        for item in history[-10:]:

            memory_context += f'{item["role"]}: {item["message"]}\n'

        full_prompt = f"""
{SYSTEM_PROMPT}

Conversation History:

{memory_context}

User:
{prompt}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        answer = response.text

        add_history("user", prompt)
        add_history("jarvis", answer)

        return answer

    except Exception as e:

        print("Gemini Error:", e)

        return "Sorry Boss, I couldn't contact Gemini."