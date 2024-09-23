# J.A.R.V.I.S - Personal Assistant

J.A.R.V.I.S (Just A Rather Very Intelligent System) is a personal assistant that listens for a wake word, processes spoken commands, and responds using a variety of natural language processing and voice synthesis tools. It integrates with APIs like OpenAI for language processing and Eleven Labs for speech synthesis, and uses libraries like `pydub` and `speech_recognition` for audio handling.

## Features

- **Wake Word Detection:** The assistant listens for a wake word to become active.
- **Voice Commands:** After the wake word is detected, J.A.R.V.I.S listens for commands and executes them.
- **Natural Language Understanding:** Uses OpenAI to understand and process spoken commands.
- **Voice Synthesis:** Responds with custom text-to-speech using Eleven Labs.
- **MP3 Playback:** Handles audio files using `pydub` and `ffmpeg` for smooth audio playback.
- **Continuous Listening:** After activation by the wake word, the system listens for further commands unless inactive for 5 minutes.

## Requirements

- Python 3.8+
- [OpenAI API Key](https://beta.openai.com/signup/)
- [Eleven Labs API Key](https://elevenlabs.io)
- FFmpeg installed and added to your system's PATH.

## Installation

1. **To start J.A.R.V.I.S.**

   Run: python main.py

