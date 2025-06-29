
# agents/content_creator_agent.py

from services.gemini_client import generate_gemini_content
from config.settings import PROMPT_PATH_CONTENT

def load_prompt_template() -> str:
    """
    Load a prompt template from the prompt file.

    Returns:
        str: The prompt template string.
    """
    with open(PROMPT_PATH_CONTENT, "r", encoding="utf-8") as f:
        return f.read()

def generate_content() -> str:
    """
    Generates text content using Gemini API based on a topic.
    
    Args:
        topic (str): Topic or subject for content generation.
    
    Returns:
        str: Generated content.
    """
    print(f"[📘] Generating content on ")

    # Load and format the prompt
    prompt_template = load_prompt_template()
    formatted_prompt = prompt_template.format()

    # Generate content using Gemini API
    content = generate_gemini_content(formatted_prompt)

    print("[✅] Content generated successfully.\n")
    return content.strip()
