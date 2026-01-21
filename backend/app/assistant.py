import requests
import audio
import screen
import helper
import voice
import datetime 

auto_delete_files = True

# 1. Set up
SERVER_URL = "http://127.0.0.1:8000/chat"

print("--- 📡 AI Client Starting ---")

# 2. Gather Data

#Record Audio
print(f"Recording Audio for 7 seconds... Say Something")
audio_file = audio.record_audio(duration=7, file_name = "client_audio.wav")

#Capture Screen
print(f"Capturing Screen...")
screen_image = screen.take_screenshot()
screen_file_name = "client_screen.png"
screen_image.save(screen_file_name)

#Text
text_input = "You are an AI assistant pair programmer. Respond to the user queries based on the provided audio and image context."


# 3. Packaging File to send to Server
text_package = {
    "text_prompt": text_input
}

files_package = {
    "audio_file": open(audio_file, "rb"),
    "image_file": open(screen_file_name, "rb")
}

# 4. SEND TO SERVER
print("🚀 Sending to Server...")

try: 
    response = requests.post(
        SERVER_URL,
        data=text_package,
        files=files_package
    )

    #Close files
    files_package["audio_file"].close()
    files_package["image_file"].close()

    # 5. Handle response
    if response.status_code == 200:
        response_data = response.json()
        ai_response = response_data["Response"]

        #Write Code solution to solution file
        code_blocks = helper.retrieve_code_from_text(ai_response)
        helper.write_code_block(code_blocks)

        print(f"Successfully received AI response: {ai_response}")

        #Clean Response
        filtered_text = helper.filter_noise_from_text(ai_response)
        voice.speak(filtered_text)

        if auto_delete_files:
            helper.delete_old_files()
    
    else:
        print(f"Error: {response.status_code}")
        print(response.text)



except Exception as e:
    print(f"Connection failed: {e}")







