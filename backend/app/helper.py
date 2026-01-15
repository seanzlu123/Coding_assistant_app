import re

def filter_noise_from_text(text):
    """
    Cleans text for speech. 
    Removes code and markdown, but KEEPS punctuation for natural pausing.
    """

    # 2. Remove Code Blocks (The big chunks)
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

def retrieve_code_from_text(text):
    """
    Extracts code blocks from the text and returns them.
    """

    #  Isolate the code blocks before filtering further
    code_block = re.findall(r"```([\s\S]*?)```", text)

    return code_block 

if __name__ == "__main__":
    sample_text = """
    Here is some sample text with code:

    ```python
    def hello_world():
        print("Hello, world!")
    ```

    And some more text here.
    """

    cleaned_text = retrieve_code_from_text(sample_text)
    print(cleaned_text)