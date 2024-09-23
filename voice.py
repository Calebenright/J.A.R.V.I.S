import requests
from decouple import config
import os
from pydub import AudioSegment
from pydub.playback import play

# Load your Eleven Labs API key from the environment variable
eleven_labs_api_key = config('ELEVEN_LABS_API_KEY')

def synthesize_voice(text, voice_id):
    """Synthesize speech using Eleven Labs API."""
    audio_file_path = "audio/output.wav"  # Path for the audio file

    # Delete the old audio file if it exists
    if os.path.exists(audio_file_path):
        os.remove(audio_file_path)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": eleven_labs_api_key
    }
    data = {
        "text": text,
        "voice": voice_id,
        "model_id": config("ELEVEN_LABS_MODEL"),
        'voice_settings': {
            'stability':0.5,
            'similarity_boost':0.9,
            'style':0.6,
        },
    }

    response = requests.post(url, headers=headers, json=data)

    with open(audio_file_path, "wb") as f:
        f.write(response.content)
    print(f"Audio saved as {audio_file_path}")
    return audio_file_path


def play_audio(file_path):
    """Play audio using pydub."""
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(file_path)
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {str(e)}")
