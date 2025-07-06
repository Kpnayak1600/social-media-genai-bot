# agents/content_creator_agent.py

from services.gemini_speech_client import generate_gemini_speech

def generate_speech():
    """
    Generates speech from text using Gemini API based on a topic.
    
    Args:
        topic (str): Content for speech generation.
    
    Returns:
        str: Generated speech.
    """
    print(f"[📘] Generating speech")
    
    # Call Gemini API
    image = generate_gemini_speech()
    
    print(f"[✅] Speech generated successfully.\n")
  
