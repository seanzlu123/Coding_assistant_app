from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import custom modules
import screen
import audio

# Load environment variables from .env file
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

class Agent:
    def __init__(self):
        self.model = "gemini-2.0-flash"
        self.client = client
        self.history = []
        
    def respond(self, text_input, audio_filename=None, screen_image=None):
        """
        Gathers all inputs (Text, Audio, Screen), packages them for Gemini,
        and returns the text response.
        """

        #Initializes parts list with just text input first
        parts = [types.Part.from_text(text=text_input)]

        #If audio input is provided, process and add to parts
        if audio_filename:
            print(f"Uploading audio file: {audio_filename}")
            uploaded_audio = self.client.files.uploaded_audio(path=audio_filename)
            parts.append(types.Part.from_audio(audio=uploaded_audio))
    
        #If screen image is provided, process and add to parts
        if screen_image:
            print("Processing screen image input")
            uploaded_screen_image = self.client.files.uploaded_screen_image(image=screen_image)
            parts.append(types.Part.from_image(image=uploaded_screen_image))

        #Generate response from Gemini model
        print("Thinking...")
        response = client.models.generate_content(
            model = self.model,
            contents = [{
                "parts": parts
            }]
        )

        return response.text

if __name__ == "__main__":
    agent = Agent()

    #Take screenshot
    screen_image = screen.take_screenshot()

    #Record audio 
    audio_filename = audio.record_audio(duration=5, file_name = "test_audio1.wav")

    answer = agent.respond(
        text_input = "You are an AI assistant pair programmer. Respond to the user based on the screenshot and audio provided.",
        audio_filename = audio_filename,
        screen_image = screen_image
    )

    print(f"AI Response: {answer}")


