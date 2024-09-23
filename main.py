import time
import random
from functions import *

def main():
    """Main loop to run the assistant."""
    play_audio("audio/chime.wav")
    while True:
        listen_for_wake_word()
        play_audio("audio/pop.wav")
        last_command_time = time.time()
        while True:
            # Check if 5 minutes of inactivity has passed
            if time.time() - last_command_time > 150:  # 5 minutes = 300 seconds
                print("1 minute of inactivity, listening for the wake word again.")
                break
            
            command = listen_for_command()  # Listen for a new command
            
            if command:
                last_command_time = time.time()  # Reset timer after command
                if command.lower() in ["exit", "stop"]:
                    if config("ELEVEN_LABS_VOICE_ID") == "SDnLQtvmhH4s69r9G7Q1":
                        goodbye_dir = "audio/goodbye/"
                        audio_files = [f for f in os.listdir(goodbye_dir) if os.path.isfile(os.path.join(goodbye_dir, f))]
                        random_file = random.choice(audio_files)
                        random_file_path = os.path.join(goodbye_dir, random_file)
                        play_audio(random_file_path)
                    else:
                        play_audio("audio/error.wav")
                    return
                
                respond(command)  # Process the command
            else:
                continue

if __name__ == "__main__":
    main()