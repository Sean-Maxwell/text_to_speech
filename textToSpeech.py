# Import the necessary modules
import speech_recognition as sr
from gtts import gTTS
import os

# Define a function to convert speech to text
def speech_to_text():
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Start recording the speech from the microphone
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # Convert the recorded speech to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Define a function to convert text to speech
def text_to_speech(text, lang='en'):
    # Initialize the gTTS object with the text to be converted
    speech = gTTS(text=text, lang=lang, slow=False)
    
    # Save the converted audio file as output.mp3
    speech.save("output.mp3")
    
    # Play the audio file using the default system audio player
    os.system("start output.mp3")

# Call the speech_to_text function to convert speech to text
text = speech_to_text()

# Call the text_to_speech function to convert the text to speech
text_to_speech(text)
