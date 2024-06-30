# AI Calendar Assistant
This project helps you manage your calendar with the help of AI. I designed it to all run locally and offline, which means you need a decent GPU to run HERMES 2 Pro. The prompts are still very finicky. Main assistant is in total_assistant.py . **THIS PROJECT ONLY WORKS ON LINUX.** While there is technically limited support for windows, one package corrupted my boot files(flash-attn), so I would not recommend it 
## Requirements
You will need SpeechRecognition, Pyaudio, and Phi assistant (instructions to come)
## Running
First, install requirements in requirements.txt. (WIP)
~~~bash
pip install -r requirements.txt
~~~

Paste this into calendar.json: {} and run cal.py. Make sure you have your microphone plugged in, and run total_assistant.py .
## How It Works
The assistant works by:
1. Converting your spoken words into text with Whipsper(via speech_recognition package)
2. Hermes 2 Pro to find the correct function and arguments
3. My python functions to find/create your event
4. Hermes 2 Pro again to take the output of that function into natural text
5. Piper to speak the text into audio