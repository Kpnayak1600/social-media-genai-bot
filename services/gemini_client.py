# # services/gemini_client.py

# from google import genai
# #import google.generativeai as genai

# from config.settings import GOOGLE_API_KEY
 
# # Configure the Gemini API with your API key
# client = genai.Client(api_key=GOOGLE_API_KEY)

# def generate_gemini_content(prompt: str) -> str:
#     """
#     Generate content using Gemini based on the input prompt.

#     Args:
#         prompt (str): The text prompt for content generation.

#     Returns:
#         str: The generated text response.
#     """
#     try:
#         print("[⚙️] Sending prompt to Gemini API...")
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents= prompt
#         )
#         print(response.text.strip())
#         return response.text.strip()
#     except Exception as e:
#         print(f"[❌] Gemini API error: {e}")
#         return "Sorry, couldn't generate content at the moment."



import os
from datetime import datetime
from config.settings import GOOGLE_API_KEY, OUTPUT_CONTENT_DIR
from google import genai

# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_gemini_content(prompt: str) -> str:
    """
    Generate content using Gemini based on the input prompt and save it to a file.

    Args:
        prompt (str): The text prompt for content generation.

    Returns:
        str: The generated text response.
    """
    try:
        print("[⚙️] Sending prompt to Gemini API...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        generated_text = response.text.strip()
        #print(generated_text)

        # # Ensure output directory exists
        # os.makedirs(OUTPUT_CONTENT_DIR, exist_ok=True)

        # # Create filename with timestamp
        # filename = f"content.txt"
        # filepath = os.path.join(OUTPUT_CONTENT_DIR, filename)

        # # Write content to file
        # with open(filepath, "w", encoding="utf-8") as f:
        #     f.write(generated_text)

        # print(f"[✅] Content saved to {filepath}")
        return generated_text

    except Exception as e:
        print(f"[❌] Gemini API error: {e}")
        return "Sorry, couldn't generate content at the moment."
