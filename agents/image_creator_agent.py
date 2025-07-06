# # agents/content_creator_agent.py

# from services.gemini_image_client import generate_gemini_image
# import os
# from config.settings import PROMPT_PATH_IMAGE

# def load_prompt_template():
#     """Load a prompt template from the config/prompts directory."""
#     with open(PROMPT_PATH_IMAGE, "r", encoding="utf-8") as f:
#         return f.read()

# def generate_image():
#     """
#     Generates image using Gemini API .
    
#     Args:
#         topic (str): Nonthing.
    
#     Returns:
#         str: Generated image.
#     """
#     print(f"[📘] Generating Image ")
    
#     # Load prompt template
#     prompt_template = load_prompt_template()
    
    
#     # Call Gemini API
#     image = generate_gemini_image(prompt_template)
    
#     print(f"[✅] Image generated successfully.\n")
  


import os
from services.gemini_image_client import generate_gemini_image
from config.settings import PROMPT_PATH_IMAGE,OUTPUT_IMAGE_DIR
from datetime import datetime
import glob

def load_prompt_templates():
    """
    Load multiple prompt templates from the image_prompt.txt file.
    Each prompt should be separated by two newlines (\n\n).
    
    Returns:
        List[str]: A list of prompt strings.
    """
    with open(PROMPT_PATH_IMAGE, "r", encoding="utf-8") as f:
        content = f.read()
        prompts = [p.strip() for p in content.split("\n\n") if p.strip()]
        return prompts
def clear_output_images():
    """
    Deletes all images from the output image directory.
    """
    if os.path.exists(OUTPUT_IMAGE_DIR):
        for file_path in glob.glob(os.path.join(OUTPUT_IMAGE_DIR, "*.png")):
            os.remove(file_path)
        print(f"[🧹] Cleared all images from {OUTPUT_IMAGE_DIR}")

def generate_image():
    """
    Iterates over all prompts and generates images using Gemini API.
    """
    print("[⚙️] Clearing previous images and generating new ones...")
    os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
    clear_output_images()
    print(f"[📘] Generating images from all prompts...")

    prompts = load_prompt_templates()
    print(f"[ℹ️] Total prompts found: {len(prompts)}")

    for i, prompt in enumerate(prompts, start=1):
        print(f"\n[⚡] Processing Prompt {i}")
        #filename = f"image_{i}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        generate_gemini_image(prompt)
        #print(prompt)

    print(f"[✅] All images generated successfully.\n")
