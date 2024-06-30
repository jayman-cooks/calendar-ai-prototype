# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from phi.assistant import Assistant
from phi.llm.ollama import Hermes
import speech_recognition as sr
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]



"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
def find_gcal_events_day(day:int, month: int, year: int, title: str, description: str, hour: int, minute: int):
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
          token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    except HttpError as error:
        print(f"An error occurred: {error}")


#make_gcal_event(1, 4, 2025, "Meeting with John", "Meet with John about the new prototype", 13, 30)
recog = sr.Recognizer()
microphone = sr.Microphone()
print("listening...")
with microphone as source:
    audio = recog.listen(source)
prompt = recog.recognize_whisper(audio)
print(prompt)
assistant = Assistant(
    tools=[find_gcal_events_day],
    show_tool_calls=False,
    llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"),
    description="You are a secretary assistant who provides helpful and concise information about the user's calendar")
# show me whats happening on 1, 4, 2025
response = assistant.run(prompt, stream=False)
print("Below is the response:")
print(response)


#print(response.split(")")[1])
#translation_table = dict.fromkeys(map(ord, '\n'), None)
#tts_line = response.split(")")[1].translate(translation_table)
#print(tts_line)
#print(f"echo '{tts_line}' | piper --model en_US-lessac-medium.onnx --output-raw | aplay -r 22050 -f S16_LE -t raw -")
#os.system("echo 'Welcome to the world of speech synthesis!' | piper --model en_US-lessac-medium --output_file welcome.wav") -- downloads model

os.system(f"echo '{response}' | piper --model en_US-lessac-medium.onnx --output-raw | aplay -r 22050 -f S16_LE -t raw -")