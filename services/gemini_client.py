# services/gemini_client.py

from google import genai
#import google.generativeai as genai

from config.settings import GOOGLE_API_KEY
 
# Configure the Gemini API with your API key
client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_gemini_content(prompt: str) -> str:
    """
    Generate content using Gemini based on the input prompt.

    Args:
        prompt (str): The text prompt for content generation.

    Returns:
        str: The generated text response.
    """
    try:
        print("[⚙️] Sending prompt to Gemini API...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= prompt
        )
        print(response.text.strip())
        return response.text.strip()
    except Exception as e:
        print(f"[❌] Gemini API error: {e}")
        return "Sorry, couldn't generate content at the moment."

