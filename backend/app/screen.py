import mss
from PIL import Image
import time

def take_screenshot():
    """
    Captures the current view of the primary monitor and converts it into a 
    memory-efficient image object.

    This function handles the complex conversion from raw screen pixels (BGR) 
    to a standard image format (RGB) and automatically resizes huge 
    Retina/4K screenshots down to 1080p to save bandwidth and speed up the AI.

    Returns:
        PIL.Image.Image: A resized, RGB-formatted image object ready to be 
                         sent to the API.
    """
    
    with mss.mss() as sct:
        #monitor = sct.monitors[1]  # Full screen
        monitor = sct.monitors[1]

        #Grab screen
        screen_image = sct.grab(monitor)

        #Convert to a PIL Image
        img = Image.frombytes("RGB", screen_image.size, screen_image.bgra, "raw", "BGRX")

        #Resize for speed
        img.thumbnail((1920, 1080))

        return img 
    
if __name__ == "__main__":
    print("Taking screenshot in 2 seconds")
    time.sleep(2)
    shot = take_screenshot()
    shot.save("test_screen.png")    
    print("Screenshot saved as test_screen.png")


