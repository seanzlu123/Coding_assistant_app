import mss
from PIL import Image
import time

def take_screenshot():
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


