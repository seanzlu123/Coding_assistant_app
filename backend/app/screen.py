import mss
from PIL import Image
import time

def take_screenshot():
    """
    Captures the primary monitor, converts to RGB, and resizes to 1080p.
    Returns: PIL.Image object (Not a file path!)
    """
    with mss.mss() as sct:
        # 1. Select Monitor 1
        monitor = sct.monitors[1]

        # 2. Grab the raw pixels
        sct_img = sct.grab(monitor)

        # 3. Convert Raw -> Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        # 4. Resize for speed/cost
        img.thumbnail((1920, 1080))

        # 5. Return the OBJECT directly
        # We do NOT save it to a file here. We hand the raw image data 
        # back to assistant.py so it can decide what to do.
        return img

if __name__ == "__main__":
    print("Taking screenshot in 2 seconds...")
    time.sleep(2)
    
    # Test the function
    shot = take_screenshot()
    
    # Since 'shot' is now an Image Object, we can save it here for testing
    shot.save("test_screen.png")    
    print("✅ Success! Saved as test_screen.png")