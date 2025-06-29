import requests
import os
from config.settings import FACEBOOK_PAGE_ID ,FACEBOOK_ACCESS_TOKEN


def post_to_facebook(video_path, caption):
    url = f"https://graph-video.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/videos"
    
    files = {
        'file': open(video_path, 'rb')
    }
    data = {
        'access_token': FACEBOOK_ACCESS_TOKEN,
        'title': caption
    }
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("✅ Facebook video posted successfully.")
    else:
        print(f"[❌] Facebook post failed: {response.text}")
