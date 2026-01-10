import sounddevice as sd
import soundfile as sf
import numpy as np  

def record_audio(duration = 5, file_name = "test_audio.wav"):
    """
    Captures audio from the default microphone and saves it as a WAV file.
    
    Args:
        duration (int): How many seconds to record. Default is 5.
        filename (str): The path where the audio file should be saved.
        
    Returns:
        str: The filename of the saved recording (to be passed to the AI).
    """

    print(f"Listening for {duration} seconds... Speak now!")

    #1. Capture audio
    sample_rate = 44100  # Standard sample rate

    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)

    #Wait for recording to finish
    sd.wait()

    #2. Save as WAV file
    sf.write(file_name, recording, sample_rate)
    print(f"Audio recording saved as {file_name}")

    return file_name

if __name__ == "__main__":
    print("Recording audio in 2 seconds")
    sd.sleep(2000)
    record_audio()
