# pip install gtts  # First install the gtts
from gtts import gTTS # first import gTTs from gtts
import os #import os module

# Function to convert text to speech
def hindi_text_to_speech(text):
    # I have Created gTTS object with Hindi language
    txt_to_spc = gTTS(text=text, lang='hi', slow=True)
    
    # Here i have saved the speech to a "speech.mp3" file
    filename = "Audio.mp3"
    txt_to_spc.save(filename)
    
    # Play the speech using default media player
    os.system(f"start {filename}")  # os For Windows

# Here is the text which i want to convert to audio 
text = "Hello world i am soumy chauhan learning python"

# Call the function
hindi_text_to_speech(text)
