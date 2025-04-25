import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_question(text: str, question: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[])

    prompt = f"""
    I have a document with the following content:
    ---
    {text}
    ---

    Now answer this question about it:
    {question}
    """

    response = chat.send_message(prompt)
    return response.text
