# AI Calendar Assistant
This project helps you manage your calendar with the help of AI. I designed it to all run locally and offline, which means you need a decent GPU to run HERMES 2 Pro. 
 **DO NOT RUN THIS PROJECT ON WINDOWS.** Despite having "limited" support for windows, the package flash-attn corrupted my boot files whenever I tried to install it(meaning my computer would have been unusable if I didn't fix it). I have not tried running it with WSL or macOS. 
## Requirements
I can only guarantee this will work on linux(ubuntu) with an nvidia GPU. It should work on macOS or with an AMD gpu, but you will likely need different packages for that. If that is the case, I would recommend installing torch and phidata according to your specs, and installing as many of the other requirements you can. 
## Running (local only version)
First, install requirements in requirements.txt.
~~~bash
pip install -r requirements.txt
~~~

Run cal.py to generate the json. This file can be transferred to send your calendar to someone else. Make sure you have your microphone plugged in, and run total_assistant.py .
## Running with Google Calendar
If you want to use Google calendar instead of local storage, there are a few more steps. 
1. Follow these instructions until you get your credentials JSON file: https://developers.google.com/calendar/api/quickstart/python. 
2. Add your Google account as a test user
3. Rename the file you just downloaded to `credentials.json` . Put this file into the calendar directory.
4. Tun gcal_total_assistant.py . You will receive a pop up to google for authorization. Follow the prompts until it says authorization was successful.
## How It Works
The assistant works by:
1. Converting your spoken words into text with Whisper(via speech_recognition package)
2. Hermes 2 Pro to find the correct function and arguments
3. My python functions to find/create your event
4. Hermes 2 Pro again to take the output of that function into natural text
5. Piper to speak the text into audio
## Troubleshooting
#### "User is not authorized"
Make sure you are signed in to your Google account, and that you have made yourself a test user.
#### Tool call 
This is an issue with Hermes, try restarting your computer. If that doesn't work, make sure you have the most recent graphics drivers
#### ALSA lib pcm_dmix.c:1032:(snd_pcm_dmix_open) unable to open slave
This is some issue between Ubuntu and the package handling the microphone. Despite all the red messages, everything works fine.

