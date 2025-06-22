# agents/content_creator_agent.py

from services.gemini_speech_client import generate_gemini_speech

def generate_speech(content_text ):
    """
    Generates speech from text using Gemini API based on a topic.
    
    Args:
        topic (str): Content for speech generation.
    
    Returns:
        str: Generated speech.
    """
    print(f"[📘] Generating speech")
    
    # Call Gemini API
    image = generate_gemini_speech(content_text)
    
    print(f"[✅] Speech generated successfully.\n")
  
