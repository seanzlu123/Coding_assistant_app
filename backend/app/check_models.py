import os
from dotenv import load_dotenv
from google import genai

#Load environment variables from .env file
load_dotenv()

# Set up Google GenAI API client
client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

def calculate_models():
    print("Calculating available models...")

    try:
        for model in client.models.list():
            print(f"- {model.name}")
            
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    calculate_models()
                  
