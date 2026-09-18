from google import genai
from config import API_KEY


client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello"
    )

    print(response.text)

except Exception as e:
    print(e)