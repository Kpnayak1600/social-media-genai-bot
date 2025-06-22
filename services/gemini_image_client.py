

# services/gemini_client.py

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from datetime import datetime
from config.settings import GOOGLE_API_KEY,  OUTPUT_IMAGE

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_gemini_image(prompt: str) -> str:
    """
    Generate image using Gemini based on the input prompt.

    Args:
        prompt (str): The text prompt for image generation.

    Returns:
        str: Path to the saved image.
    """
    try:
        print("[⚙️] Sending prompt to Gemini API...")
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                image = Image.open(BytesIO(image_data))

                # Create filename and path
                # filename = f"image.png"
                # os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
                # image_path = os.path.join(OUTPUT_IMAGE_DIR, filename)

                # Save image
                image.save(OUTPUT_IMAGE)
                print(f"✅ Image saved to {OUTPUT_IMAGE}")
                

    except Exception as e:
        print(f"[❌] Gemini API error: {e}")
        return "Sorry, couldn't generate content at the moment."
