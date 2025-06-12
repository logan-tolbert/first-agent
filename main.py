import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
model = "gemini-2.0-flash-001"
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error: Prompt must be provided as a command-line argument.")
    sys.exit(1)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

try:
    response = client.models.generate_content(
        model=model,
        contents=messages
    )

    if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        print(f'User prompt: {user_prompt}')
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:   
        print(response.text)
   

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
