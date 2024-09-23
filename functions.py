import speech_recognition as sr
import pyttsx3
from langchain_openai import OpenAI  # Correct import for OpenAI
from langchain.chains import ConversationChain  # Correct import for ConversationChain
from decouple import config
from voice import *
import time

openai_api_key = config('OPENAI_API_KEY')
llm = OpenAI(api_key=openai_api_key)
engine = pyttsx3.init()
conversation = ConversationChain(llm=llm)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def generate_response(input_text):
    """Generate a response using the LLM."""
    response = llm.invoke(input_text)
    print(response)
    return response

def listen_for_wake_word():
    """Listen for the wake word indefinitely in a low power state."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise
        print("Listening for wake word...")
        
        while True:
            try:
                # Listen for a short duration to minimize power usage
                audio = recognizer.listen(source, timeout=0.5, phrase_time_limit=1)  # Very short timeout
                command = recognizer.recognize_google(audio)
                if config("WAKE_WORD") in command.lower():  # Wake word
                    print("Wake word detected!")
                    return
            except sr.UnknownValueError:
                # Ignore unknown value errors, continue listening
                continue
            except sr.RequestError:
                speak("Sorry, I'm having trouble with the service.")
                continue
            except sr.WaitTimeoutError:
                # Handle the timeout case gracefully
                continue  # Just loop again to listen for the wake word

def listen_for_command():
    """Listen for a command after the wake word is detected."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            play_audio("audio/thud.wav")
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            play_audio("audio/error.wav")
            return ""
        
def should_take_action(response):
    """Evaluate the LLM's response to determine if an action is needed."""
    return "yes" in response.lower()

def handle_incoming_data(data):
    """Process incoming data and determine if action is needed."""
    # Append the new data to the conversation
    prompt = f"Data received: {data}. Should I take any action? Please respond with 'yes' or 'no'."
    response = generate_response(prompt)
    
    if should_take_action(response):
        speak("Taking action based on the received data.")
        # Add your action logic here
    else:
        speak("No action needed at this time.")

def respond(data):
    """Process incoming data and determine if action is needed."""
    # Append the new data to the conversation
    role = config('AI_ROLE')
    response = generate_response(f"{role} Respond to this and keep it concise: {data}")
    get_voice(response)

def get_voice(text):
    if config('IS_CUSTOM_VOICE'):
        try:
            audio_file = synthesize_voice(text, config('ELEVEN_LABS_VOICE_ID'))
            
            if audio_file:
                play_audio(audio_file)
        except:
            speak(text)
    else:
        speak(text)


