from google import genai
from config import API_KEY

client = genai.Client(
    api_key=API_KEY
)

print("Jarvis AI Ready! Type 'exit' to quit.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Jarvis: Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        print("\nJarvis:", response.text)

    except Exception as e:
        print("Error:", e)