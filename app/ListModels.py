import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def list_models():
    models = genai.list_models()
    for model in models:
        print(model)

list_models()
