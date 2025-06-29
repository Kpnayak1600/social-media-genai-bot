# master_agents/social_media_scheduler.py

from datetime import datetime

from services.social_media_API.Instagram_api import post_to_instagram
from services.social_media_API.facebook_api import post_to_facebook
from services.social_media_API.youtube_api import post_to_youtube

def schedule_post(video_path, caption,title):
    """
    Called from main.py to post at specific datetime.
    """
    print("[🤖] Master Agent 2: Posting Instagram ...")
    post_to_instagram(video_path, caption)
    print("[🤖] Master Agent 2: Posting facebook ...")
    post_to_facebook(video_path, caption)
    print("[🤖] Master Agent 2: Posting youtube...")
    post_to_youtube(video_path, caption,title)

