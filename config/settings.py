# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# === youtube API CREDENTIALS ===
YOUTUBE_CLIENT_SECRET_FILE = os.getenv("YOUTUBE_CLIENT_SECRET_FILE")

# === BASE DIRECTORY ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# === PROMPT TEMPLATE PATHS ===
PROMPT_PATH_CAPTION = os.path.join(BASE_DIR, "config", "prompts", "caption_prompt.txt")
PROMPT_PATH_IMAGE = os.path.join(BASE_DIR, "config", "prompts", "image_prompt.txt")
PROMPT_PATH_CONTENT = os.path.join(BASE_DIR, "config", "prompts", "content_prompt.txt")
PROMPT_PATH_Title = os.path.join(BASE_DIR, "config", "prompts", "title_prompt.txt")

# === OUTPUT PATHS ===
OUTPUT_IMAGE = os.path.join(BASE_DIR, "outputs", "images","image.png")
OUTPUT_AUDIO= os.path.join(BASE_DIR, "outputs", "audios","out.wav")
OUTPUT_POST = os.path.join(BASE_DIR, "outputs", "posts","video.mp4")

# === TOPIC OF PROMPTS ===
TOPIC_OF_PROMPTS = "Motivational quote of the day"

# === GEMINI API ===
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# === INSTAGRAM CREDENTIALS ===
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# === FACEBOOK CREDENTIALS ===
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS")
FACEBOOK_PAGE_ID = os.getenv("facebook_page_id")

# === TIMING CONFIGS (as integers for formatting and scheduling) ===
DAILY_POST_HOUR = 22  # 10 PM
DAILY_POST_MINUTE = 34
