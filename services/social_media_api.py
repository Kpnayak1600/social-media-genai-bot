# services/social_media_api.py

from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

def post_to_instagram(video_path: str, caption: str):
    """
    Uploads a video to Instagram with a caption.
    """
    try:
        print("[📲] Logging into Instagram...")
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        print(f"[📤] Uploading video: {video_path}")
        cl.clip_upload(video_path, caption=caption)
        print("[✅] Posted to Instagram.")

    except Exception as e:
        print(f"[❌] Instagram upload failed: {e}")
