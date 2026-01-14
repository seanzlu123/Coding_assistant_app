from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai import types
import os

# Import custom modules
import screen
import audio
import voice

# Load environment variables from .env file
current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent.parent / '.env'
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") 

if not api_key:
    raise ValueError("API Key not found.")

client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

class Agent:
    def __init__(self):
        self.default_response_mode = True # True: respond with text; False: respond with voice
        self.model = "gemini-2.5-flash"
        self.client = client
        self.history = []
    
    def toggle_response_mode(self):
        '''Toglges between text and voice response modes.'''
        self.default_response_mode = not self.default_response_mode
        if self.default_response_mode:
            print(f"Response mode set to TEXT.")
        else:
            print(f"Response mode set to VOICE.")
            
    def upload_image(self, image_path):
        '''Uploads a image file using Gemini Files API 
        and returns the uploaded file reference.'''

        image = self.client.files.upload(file=image_path)
        return image

    def upload_audio(self, audio_path):
        '''Uploads an audio file using Gemini Files API 
        and returns the uploaded file reference.'''

        print(f"Uploading audio from: {audio_path}")
        audio = self.client.files.upload(file=audio_path)
        return audio

    def respond(self, text_input, audio_filename=None, screen_image=None):
      
        """
        Gathers all inputs (Text, Audio, Screen), packages them for Gemini,
        and returns the text response.
        """

        my_contents = []
        if audio_filename:
            audio_file = self.upload_audio(audio_filename)
            my_contents.append(audio_file)
            print("Audio file uploaded.")

        if screen_image:
            if not isinstance(screen_image, str):
                print("Detected PIL Image object. Saving to file...")
                temp_filename = "temp_screen.png"
                screen_image.save(temp_filename)
                screen_image = temp_filename # Update variable to be the PATH string
                
            image_file = self.upload_image(screen_image)
            my_contents.append(image_file)
            print("Screen image uploaded.")
        
        if text_input:
            my_contents.append(text_input)
            print("Text input added.")

        response = client.models.generate_content(model=self.model,contents = my_contents)

        if response.text and self.default_response_mode:
            return response.text
        else:
            voice.speak(response.text)
            return None

if __name__ == "__main__":
    agent = Agent()
    agent.toggle_response_mode()  # Switch to voice mode

    #Take screenshot
    image_path = screen.take_screenshot()

    #Record audio 
    audio_path= audio.record_audio(duration=5, file_name = "test_audio1.wav")

    answer = agent.respond(
        text_input = "You are an AI assistant pair programmer. Respond to the user based on the screenshot and audio provided.",
        audio_filename = audio_path,
        screen_image = image_path
    )



