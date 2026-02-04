import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

elevenlabs_api_key = os.getenv("ELEVEN_LAB_KEY")

# --- FIX 1: This needed quotes to be a string ---
voice_id = "KgETZ36CCLD1Cob4xpkv" 

def speak(text):
    """
    Converts text to audio and plays it using ELEVEN LABS AI voice. 
    """
    if not text:
        print("No text provided for speech synthesis.")
        return
    
    print(f"AI is saying: {text}")

    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": elevenlabs_api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        }
        
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error with ElevenLabs: {response.status_code} - {response.text}")

        # Save the binary audio data to a file
        audio_file = "output.mp3"
        
        #write binary to file 
        with open(audio_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print(f"Audio saved to {audio_file}")

        # This simulates double-clicking the file to open it in your default player
        os.startfile(audio_file)
        
        #Sleep to let the audio start playing before script ends
        time.sleep(2) 

    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")

if __name__ == "__main__":
    sample_text = "Hello! I am now using the Eleven Labs API. The system is fully operational."
    speak(sample_text)