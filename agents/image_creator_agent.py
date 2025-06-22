# agents/content_creator_agent.py

from services.gemini_image_client import generate_gemini_image
import os
from config.settings import PROMPT_PATH_IMAGE

def load_prompt_template():
    """Load a prompt template from the config/prompts directory."""
    with open(PROMPT_PATH_IMAGE, "r", encoding="utf-8") as f:
        return f.read()

def generate_image():
    """
    Generates image using Gemini API .
    
    Args:
        topic (str): Nonthing.
    
    Returns:
        str: Generated image.
    """
    print(f"[📘] Generating Image ")
    
    # Load prompt template
    prompt_template = load_prompt_template()
    
    
    # Call Gemini API
    image = generate_gemini_image(prompt_template)
    
    print(f"[✅] Image generated successfully.\n")
  
