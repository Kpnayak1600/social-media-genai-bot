# master_agents/instagram_post_creator.py

from services.gemini_client import generate_gemini_content
from services.video_creator import create_video_from_image_and_audio
from config.settings import PROMPT_PATH_CAPTION
from config.settings import OUTPUT_IMAGE, OUTPUT_AUDIO

def generate_instagram_caption() -> str:
    """
    Generate an Instagram caption using Gemini API.

    Args:
        content (str): Base content or message.

    Returns:
        str: Stylized caption suitable for social media.
    """
    print("[📝] Generating Instagram caption...")

    # Load caption prompt
    prompt_template_path = PROMPT_PATH_CAPTION
    with open(prompt_template_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    #prompt = prompt_template.replace("{content}", content)
    caption = generate_gemini_content(prompt_template)
    return caption


def create_instagram_post() -> dict:
    """
    Orchestrates the creation of all Instagram post assets.

    Args:
        content (str): Text content from Content Agent.

    Returns:
        dict: Dictionary containing image, audio, video, and caption paths/text.
    """
    print("[🤖] Master Agent 1: Creating Instagram post...")

    # 1. Generate image
    image_path = OUTPUT_IMAGE
    # 2. Generate speech/audio
    audio_path = OUTPUT_AUDIO
    # 3. Generate caption
    caption = generate_instagram_caption()
    #print(caption)

    # 4. Combine into video
    #create_video_from_image_and_audio(image_path, audio_path)
    create_video_from_image_and_audio(audio_path)

    print("[✅] Post creation complete.")

    return caption