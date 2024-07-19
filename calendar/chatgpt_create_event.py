import json
from openai import OpenAI
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
with open("openai_tok.json", "r") as token:
    api_tok = json.load(token)["Token"]

tools = [
  {
    "type": "function",
    "function": {
      "name": "create_event",
      "description": "Create an event in the calendar",
      "parameters": {
        "type": "object",
        "properties": {
          "day": {
            "type": "integer",
            "description": "The day of the event",
          },
          "month": {
                "type": "integer",
                "description": "The month of the event",
          },
          "year": {
                "type": "integer",
                "description": "The year of the event",
          },
          "title": {
                "type": "string",
                "description": "The title of the event",
          },
          "description": {
                "type": "string",
                "description": "The description of the event",
          },
          "hour": {
                "type": "integer",
                "description": "The hour of the event in 24 hour time",
          },
          "minute": {
                "type": "integer",
                "description": "The year of the event",
          },
    #"required": ["day", "month", "year"]
        }
      }
    }
  }
]


def make_gcal_event(day: int, month: int, year: int, title: str, description: str, hour: int, minute: int):
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
        event = {
            'summary': title,
            'description': description,
            'start': {
                'dateTime': f'{year}-{month}-{day}T{hour}:{minute}:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': f'{year}-{month}-{day}T{hour}:{minute}:00-07:00',
                'timeZone': 'America/Los_Angeles',
            }
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        return f"created an event, {title} on {month}, {day}, {year}, with a description {description} at {hour}:{minute}"


    except HttpError as error:
        print(f"An error occurred: {error}")


# refresh token.json if scopes get changed
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]


creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
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



url = "https://jamsapi.hackclub.dev/openai"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_tok, base_url=url,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Create an event for the day April 1 2025, with the title 'Testing', a description 'hello from chatgpt!', at 13:45",
        }
    ],
    model="gpt-3.5-turbo",
    tools=tools,
    tool_choice="auto"
)
print(chat_completion)
print(chat_completion.choices[0].message.tool_calls[0].function.arguments)
func_resp = chat_completion.choices[0].message.tool_calls[0].function
json_rsp = json.loads(func_resp.arguments)
if func_resp.name == "create_event":
    gcal_resp = make_gcal_event(json_rsp["day"], json_rsp["month"], json_rsp["year"], json_rsp["title"], json_rsp["description"], json_rsp["hour"], json_rsp["minute"])
else:
    gcal_resp = "There was an error. Try rephrasing"
print(gcal_resp)

chat_completion2 = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"You are a calendar assistant. Rephrase this information for the user: {gcal_resp}",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion2.choices[0].message.content)