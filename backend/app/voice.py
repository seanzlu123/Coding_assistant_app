from gtts import gTTS
import os
import time 

def speak(text):
    """
    Converts text to audio and plays it using system default player.
    """

    if not text:
        print("No text provided for speech synthesis.")
        return
    
    print(f"AI is saying: {text}")

    try:
        filename = f"response_{int(time.time())}.mp3"
        tts = gTTS(text=text, lang='en', tld='us')
        tts.save(filename)

        os.startfile(filename)
    
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")

if __name__ == "__main__":
    sample_text = "Hello! This is a test of the text to speech functionality."
    speak(sample_text)

        


