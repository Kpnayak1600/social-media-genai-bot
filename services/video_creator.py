# # services/video_creator.py

# from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
# import os

 
# def create_video_from_image_and_audio(image_path: str, audio_path: str, duration: int = None) -> str:
#     """
#     Combines an image and audio file into a video using MoviePy.

#     Args:
#         image_path (str): Path to the image file.
#         audio_path (str): Path to the audio file.
#         duration (int, optional): Duration of the video in seconds. If None, use audio duration.

#     Returns:
#         str: Path to the saved video file.
#     """
#     print("[🎬] Creating video from image and audio...")

#     # Load audio
#     audio_clip = AudioFileClip(audio_path)
#     audio_duration = audio_clip.duration

#     # Determine duration
#     final_duration = duration or audio_duration

#     # Load image and set duration
#     image_clip = ImageClip(image_path, duration=final_duration)

#     # Resize to Instagram square (1080x1080)
#     #image_clip = image_clip.resize((1080, 1080))

#     # Set audio to image clip
#     video_clip = image_clip.set_audio(audio_clip) 

#     # Export path
#     #filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
#     filename = "video.mp4"
#     video_path = os.path.join("./outputs/posts/", filename)
#     os.makedirs("./outputs/posts/", exist_ok=True)
    

#     # Export video
#     video_clip.write_videofile(video_path, fps=24, codec='libx264', audio_codec='aac')

#     print(f"[✅] Video created: {video_path}")
    


from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os
from config.settings import OUTPUT_IMAGE_DIR, OUTPUT_POST_DIR
from config.settings import OUTPUT_IMAGE, OUTPUT_AUDIO

def create_video_from_image_and_audio(audio_path: str,duration_per_image: int = 3) -> str:
    """
    Combines multiple images and an audio file into a single video using MoviePy.

    Args:
        audio_path (str): Path to the audio file.
        duration_per_image (int): Duration (in seconds) each image is shown.

    Returns:
        str: Path to the saved video file.
    """
    print("[🎬] Creating video from multiple images and audio...")

    # Load audio clip
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    # Get all image paths
    image_files = sorted([
        os.path.join(OUTPUT_IMAGE_DIR, f)
        for f in os.listdir(OUTPUT_IMAGE_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ])

    if not image_files:
        print("[❌] No image files found in output image directory.")
        return None

    # Calculate how many images we need
    required_images = max(1, int(audio_duration // duration_per_image))
    total_images = len(image_files)

    if total_images < required_images:
        # Repeat images if not enough to cover full duration
        image_files = (image_files * ((required_images // total_images) + 1))[:required_images]

    # Create image clips
    image_clips = [
        ImageClip(img_path)
        .set_duration(duration_per_image)
        .set_position("center")
        for img_path in image_files
        # ImageClip(img_path)
        # .set_duration(duration_per_image)
        # .resize(height=720)  # Resize for 720p output
        # .set_position("center")
        # for img_path in image_files
    ]

    # Concatenate all image clips
    video_clip = concatenate_videoclips(image_clips, method="compose")
    video_clip = video_clip.set_audio(audio_clip).set_duration(audio_duration)

    # Export video
    os.makedirs(OUTPUT_POST_DIR, exist_ok=True)
    video_path = os.path.join(OUTPUT_POST_DIR, "video.mp4")
    video_clip.write_videofile(video_path, fps=24, codec="libx264", audio_codec="aac")

    print(f"[✅] Video created at: {video_path}")
    return video_path

