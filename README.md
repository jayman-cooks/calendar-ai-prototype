# AI Calendar Assistant
This project helps you manage your calendar with the help of AI. I designed it to all run locally and offline, which means you need a decent GPU to run HERMES 2 Pro. The prompts are still very finicky. Main assistant is in total_assistant.py . **THIS PROJECT ONLY WORKS ON LINUX.** (maybe MacOS) While there is technically limited support for windows, one package corrupted my boot files(flash-attn), so I would not recommend it. I have not tried running it with WSL. 
## Requirements
I can only guarantee this will work on linux(ubuntu) with an nvidia GPU. It should work on MacOS or with an AMD gpu, but you will likely need different packages for that. 
## Running (local only version)
First, install requirements in requirements.txt.
~~~bash
pip install -r requirements.txt
~~~

Paste this into calendar.json: {} and run cal.py. Make sure you have your microphone plugged in, and run total_assistant.py . There is a bug that outputs audio errors, even though the rest works. 
## Running with Google Calendar
If you want to use Google calendar instead of local storage, there are a few more steps. 
Follow these instructions until you get your credentials JSON file: https://developers.google.com/calendar/api/quickstart/python. Rename the file you just downloaded to `credentials.json` . Put this file into the calendar directory. After that, you should be good to run gcal_total_assistant.py and follow the prompts. 
## How It Works
The assistant works by:
1. Converting your spoken words into text with Whipsper(via speech_recognition package)
2. Hermes 2 Pro to find the correct function and arguments
3. My python functions to find/create your event
4. Hermes 2 Pro again to take the output of that function into natural text
5. Piper to speak the text into audio