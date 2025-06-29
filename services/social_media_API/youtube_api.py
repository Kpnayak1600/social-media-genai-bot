import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config.settings import YOUTUBE_CLIENT_SECRET_FILE

# Required OAuth 2.0 scope for uploading videos to YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    """
    Authenticates with YouTube using OAuth 2.0 and returns the YouTube API client.
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        YOUTUBE_CLIENT_SECRET_FILE, SCOPES
    )
    
    # Use local server to handle OAuth flow (replaces deprecated run_console)
    credentials = flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message='')

    youtube = build("youtube", "v3", credentials=credentials)
    return youtube

def post_to_youtube(video_path, caption,title):
    """
    Uploads a video to YouTube.

    Args:
        video_path (str): Path to the video file to upload.
        caption (str): Description of the video.

    Returns:
        str: URL of the uploaded YouTube video or None if failed.
    """
    try:
        youtube = authenticate_youtube()

        print("[📤] Uploading video to YouTube...")

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": caption,
                    "tags": ["Sanskrit", "Hinduism", "AI", "Motivation"]
                },
                "status": {
                    "privacyStatus": "public"
                }
            },
            media_body=MediaFileUpload(video_path, resumable=True)
        )

        response = request.execute()
        video_url = f"https://youtube.com/watch?v={response['id']}"
        print(f"[✅] YouTube video uploaded: {video_url}")
        return video_url

    except Exception as e:
        print(f"[❌] YouTube upload failed: {e}")
        return None
