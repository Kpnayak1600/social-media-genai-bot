# master_agents/social_media_scheduler.py

from datetime import datetime

from services.social_media_api import post_to_instagram

def schedule_post(video_path, caption):
    """
    Called from main.py to post at specific datetime.
    """
    post_to_instagram(video_path, caption)

