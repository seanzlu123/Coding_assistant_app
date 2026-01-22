from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware # <--- NEW
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai import types
import shutil
import requests
import os


# --- 1. ROBUST ENV LOADING ---
# Get the path to 'backend/app'
current_dir = Path(__file__).resolve().parent

# Go up two levels: backend/app -> backend -> ROOT
env_path = current_dir.parent.parent / '.env'
print(f"Loading .env from: {env_path}") # Debug print
load_dotenv(dotenv_path=env_path)

# --- 2. GET API KEY ---
# Check BOTH common names to be safe
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # If this prints, check your .env file again!
    raise ValueError(f"❌ API Key not found in {env_path}")

print("✅ API Key found. Starting Server...")

#Initialize Clients
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = genai.Client(api_key=api_key)

#Create chat session with Gemini
chat = client.chats.create(model = "gemini-2.5-flash")

@app.post("/chat")
async def chat_endpoint(
    text_prompt: str = Form(...),
    audio_file: UploadFile = File(None),
    image_file: UploadFile = File(None)
):
    contents = []

    print(f"User said: {text_prompt}")


    # 1. Handle Audio: Save -> Upload -> Append
    if audio_file:
        print(f"Got audio file: {audio_file}")
        temp_audio_name = f"temp_{audio_file.filename}"
        with open(temp_audio_name, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        print(f"Uploading audio file to Gemini...")
        uploaded_audio = client.files.upload(file = temp_audio_name)
        contents.append(uploaded_audio)

    # 2. Handle Image: Save -> Upload -> Append
    if image_file:
        print(f"Got image file: {image_file}")
        temp_image_name = f"temp_{image_file.filename}"
        with open(temp_image_name, "wb") as buffer:
            shutil.copyfileobj(image_file.file, buffer)
        
        print(f"Uploading image file to Gemini...")
        uploaded_image = client.files.upload(file = temp_image_name)
        contents.append(uploaded_image)

    # 3. Lastly, handle User Text input
    if text_prompt:
        contents.append(text_prompt)

    # 4. Generate response from Gemini
    print(f"Gemini: Generating Response")
    ai_response = chat.send_message(message=contents)
    

    return {"Response": ai_response.text}

