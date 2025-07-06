

# # services/gemini_client.py

# from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO
# import os
# from datetime import datetime
# from config.settings import GOOGLE_API_KEY,  OUTPUT_IMAGE

# client = genai.Client(api_key=GOOGLE_API_KEY)

# def generate_gemini_image(prompt: str) -> str:
#     """
#     Generate image using Gemini based on the input prompt.

#     Args:
#         prompt (str): The text prompt for image generation.

#     Returns:
#         str: Path to the saved image.
#     """
#     try:
#         print("[⚙️] Sending prompt to Gemini API...")
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-preview-image-generation",
#             contents=prompt,
#             config=types.GenerateContentConfig(
#                 response_modalities=['TEXT', 'IMAGE']
#             )
#         )

#         for part in response.candidates[0].content.parts:
#             if part.inline_data is not None:
#                 image_data = part.inline_data.data
#                 image = Image.open(BytesIO(image_data))

#                 # Create filename and path
#                 # filename = f"image.png"
#                 # os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
#                 # image_path = os.path.join(OUTPUT_IMAGE_DIR, filename)

#                 # Save image
#                 image.save(OUTPUT_IMAGE)
#                 print(f"✅ Image saved to {OUTPUT_IMAGE}")
                

#     except Exception as e:
#         print(f"[❌] Gemini API error: {e}")
#         return "Sorry, couldn't generate content at the moment."


# services/gemini_client.py

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
import glob
from datetime import datetime
from config.settings import GOOGLE_API_KEY, OUTPUT_IMAGE_DIR

# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

# def clear_output_images():
#     """
#     Deletes all images from the output image directory.
#     """
#     if os.path.exists(OUTPUT_IMAGE_DIR):
#         for file_path in glob.glob(os.path.join(OUTPUT_IMAGE_DIR, "*.png")):
#             os.remove(file_path)
#         print(f"[🧹] Cleared all images from {OUTPUT_IMAGE_DIR}")

def generate_gemini_image(prompt) -> list:
    """
    Generate multiple images using Gemini based on the input prompt.

    Args:
        prompt (str): The text prompt for image generation.
        count (int): Number of images to generate.

    Returns:
        list: List of paths to the saved images.
    """
    image_paths = []
    try:
        # print("[⚙️] Clearing previous images and generating new ones...")
        # os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
        # clear_output_images()

        for i in range(1):
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

                    # Unique filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
                    filename = f"image_{timestamp}.png"
                    image_path = os.path.join(OUTPUT_IMAGE_DIR, filename)

                    image.save(image_path)
                    image_paths.append(image_path)
                    print(f"[✅] Image saved to {image_path}")
    except Exception as e:
        print(f"[❌] Gemini API error: {e}")

    return image_paths
