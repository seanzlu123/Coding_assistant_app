import re

example_string = "AI is saying: Yes, I can definitely take a look at your code. It looks like you're encountering a `TypeError` on line 99 of `assistant.py`:\n\n```python\nimage_path = screen.take_screenshot(filename=\"screenshot.png\")\n```\n\nThe error message `TypeError: take_screenshot() got an unexpected keyword argument 'filename'` indicates that the `screen.take_screenshot()` function does not accept a `filename` argument.\n\nTo fix this, you'll need to:\n\n1. **Check the `screen` module's documentation or source code:** Find out what arguments, if any, the `take_screenshot()` function expects.\n2. **Adjust your call:**\n   * It's possible `take_screenshot()` doesn't take any arguments and saves the screenshot to a default location (or returns the path directly).\n   * Or, it might expect a different argument name for the output file (e.g., `path`, `output_file`).\n\nFor example, if it doesn't take a `filename` argument, you might just call it as:\n\n```python\nimage_path = screen.take_screenshot()\n`"

def text_cleaning_function(text):
    """
    Cleans text for speech. 
    Removes code and markdown, but KEEPS punctuation for natural pausing.
    """
    # 1. Remove Code Blocks (The big chunks)
    # We replace them with a spoken phrase so the user knows to look at the screen.
    text = re.sub(r"```[\s\S]*?```", " ... check the code on your screen ... ", text)
    
    # 2. Remove Inline Code (Single backticks)
    text = re.sub(r"`", "", text)
    
    # 3. Remove Formatting (Bold/Italic), but KEEP punctuation (.,?!)
    # We only remove asterisks (*), underscores (_), and hashes (#)
    text = re.sub(r"[\*_#]", "", text) 
    
    # 4. Collapse whitespace (newlines -> space)
    text = re.sub(r"\s+", " ", text)
    
    return text.strip()

print(text_cleaning_function(example_string))