
# agents/content_creator_agent.py

from services.gemini_client import generate_gemini_content
from config.settings import PROMPT_PATH_Title

def load_prompt_template() -> str:
    """
    Load a prompt template from the prompt file.

    Returns:
        str: The prompt template string.
    """
    with open(PROMPT_PATH_Title, "r", encoding="utf-8") as f:
        return f.read()

def generate_title() -> str:
    """
    Generates title using Gemini API .
    
    Args:
        topic (str): Title prompt.
    
    Returns:
        str: Generated content.
    """
    print(f"[📘] Generating Title ")

    # Load and format the prompt
    prompt_template = load_prompt_template()
    formatted_prompt = prompt_template.format()

    # Generate content using Gemini API
    content = generate_gemini_content(formatted_prompt)

    print("[✅] Content generated successfully.\n")
    return content.strip()
