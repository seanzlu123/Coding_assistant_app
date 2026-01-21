import re
import time
import os
import glob

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
    matches = re.findall(r"```(?:[\w]*\n)?([\s\S]*?)```", text)

    return matches

def write_code_block(code_blocks): 
    """
    Takes code blocks and writes to a solution file
    """

    filename = f"solution_{int(time.time())}.py"
    with open(filename, "w") as file:
        file.write("\n\n".join(code_blocks))

def delete_old_files():
    """
    Automatically deletes files containing patterns listed in patterns
    """

    patterns = ["response_*", "client_*.*", "temp_*.*"] 

    for pattern in patterns:
        for file_path in glob.glob(pattern):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            
            except Exception as e:
                print(e)

        

        