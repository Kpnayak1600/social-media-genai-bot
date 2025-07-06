# main.py

from agents.content_creator_agent import generate_content
from agents.image_creator_agent import generate_image
from agents.title_creator_agent import generate_title
from agents.speech_creator_agent import generate_speech
from master_agents.instagram_post_creator import create_instagram_post
from master_agents.social_media_handler import schedule_post
from services.schedular import run_scheduled_task
from config.settings import OUTPUT_POST
from config.settings import DAILY_POST_HOUR, DAILY_POST_MINUTE


def main():
    print("[🚀] Starting Multi-Agent Social Media Workflow...")

    # 1. Generate content (text)
    # print("[✍️ ] Generating content...")
    # content_text = generate_content()

    # # 2. Generate image using content
    # print("[🖼️ ] Generating image from text...")
    # generate_image()

    # #3. Generate speech using content
    # print("[🔊] Generating speech from text...")
    # generate_speech()
    
    # 4. Generate yoututbe title
    print("[🎗️] Generating Title...")
    title = generate_title()
    print(title)

    #5. Create Instagram-ready post (caption + image + audio/video)
    # print("[🎞️ ] Creating Instagram post...")
    # caption = create_instagram_post()

    # 6. Schedule the post to be published at 9 PM today

    

    print("[📅] Scheduling post for 9 PM today...")
    print("[📲] Posting to Social Media...")
    schedule_post(OUTPUT_POST, "SamudraManthan",title)

    # print("[✅] Workflow completed successfully!")

if __name__ == "__main__": 
    #run_scheduled_task(main, time_str=f"{DAILY_POST_HOUR}:{DAILY_POST_MINUTE}")
    main()
