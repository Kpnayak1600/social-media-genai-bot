# services/video_creator.py

from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
import os

 
def create_video_from_image_and_audio(image_path: str, audio_path: str, duration: int = None) -> str:
    """
    Combines an image and audio file into a video using MoviePy.

    Args:
        image_path (str): Path to the image file.
        audio_path (str): Path to the audio file.
        duration (int, optional): Duration of the video in seconds. If None, use audio duration.

    Returns:
        str: Path to the saved video file.
    """
    print("[🎬] Creating video from image and audio...")

    # Load audio
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    # Determine duration
    final_duration = duration or audio_duration

    # Load image and set duration
    image_clip = ImageClip(image_path, duration=final_duration)

    # Resize to Instagram square (1080x1080)
    #image_clip = image_clip.resize((1080, 1080))

    # Set audio to image clip
    video_clip = image_clip.set_audio(audio_clip) 

    # Export path
    #filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    filename = "video.mp4"
    video_path = os.path.join("./outputs/posts/", filename)
    os.makedirs("./outputs/posts/", exist_ok=True)
    

    # Export video
    video_clip.write_videofile(video_path, fps=24, codec='libx264', audio_codec='aac')

    print(f"[✅] Video created: {video_path}")
    

