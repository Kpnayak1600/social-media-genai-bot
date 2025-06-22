

from pathlib import Path
import wave
from google import genai
from google.genai import types
from config.settings import GOOGLE_API_KEY

# Configure the Gemini API with your API key
client = genai.Client(api_key=GOOGLE_API_KEY)

# Set up the wave file to save the output
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

def generate_gemini_speech(content_text: str) -> str:
    try:
        print("[⚙️] Sending content to Gemini API for speech generation...")
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=content_text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name='Kore',
                        )
                    )
                ),
            )
        )

        # Extract audio data
        data = response.candidates[0].content.parts[0].inline_data.data

        # Create output directory if it doesn't exist
        audio_dir = Path("outputs/audios")
        audio_dir.mkdir(parents=True, exist_ok=True)

        # Define full path for audio file
        file_path = audio_dir / "out.wav"

        # Save wave file
        wave_file(str(file_path), data)
        print(f"[✅] Audio saved at {file_path}")
        return str(file_path)

    except Exception as e:
        print(f"[❌] Gemini API error: {e}")
        return "Sorry, couldn't generate speech at the moment."

