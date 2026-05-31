import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Use your API key from https://makersuite.google.com/app/apikey
genai.configure(api_key=GEMINI_API_KEY)

def chat_with_gemini(prompt):
    # ✅ Use a valid model
    model = genai.GenerativeModel("gemini-2.5-flash")  
    response = model.generate_content(prompt)
    return response.text

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    reply = chat_with_gemini(user_input)
    print("Bot:", reply)