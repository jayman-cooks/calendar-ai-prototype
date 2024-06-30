

import json
import httpx

from phi.assistant import Assistant
from phi.llm.ollama import Hermes
import speech_recognition as sr
import os
import calendar as calp
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def find_events(day: int = 1, month: int = 4, year: int = 2024) -> str:
    """Use this function to find current events

    Args:
        day (int): The day of the event
        month (int): The number of the month of the event
        year (int): The year of the event

    Returns:
        str: The descriptions. titles, and times of the events.
    """
    with open('calendar.json', 'r') as openfile:
        calendar = json.load(openfile)
    events = calendar[str(year)][str(month)][str(day)]
    return_list = []
    for i in range(len(events)):
        return_list.append([events[str(i)]["Title"], events[str(i)]["Description"],
                            f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}", [], events[str(i)]["Priority"]])
        for y in range(len(events[str(i)]["People"])):
            return_list[i][3].append(events[str(i)]["People"][str(y)])
    print(return_list)
    print(f"here are all the events: {calendar[str(year)][str(month)][str(day)]}")
    return_str = f"You have {len(return_list)} events for that day:"
    for i in range(len(return_list)):
        temp_str = ""
        temp_str += f" #{i + 1} {return_list[i][0]} - {return_list[i][1]} with priority value {return_list[i][4]} at {return_list[i][2]} with {len(return_list[i][3])} people:"
        for y in range(len(return_list[i][3])):
            temp_str += f" {return_list[i][3][y]}"
        temp_str += "."
        return_str += temp_str
    return return_str


def find_events_in_week(day: int, month: int, year: int) -> str: # potential bug if week extends out of month
    """Use this function to find all events in a given week

    Args:
        day (int): The first day of the week
        month (int): The month of the first day of the week
        year (int): The year of the first day of the week

    Returns:
        str: The descriptions. titles, and times of the events.
    """
    return_list = []
    bug_fix = 0 # to fix a bug that prevented it from searching correct days for month overflow
    days_in_month = calp.monthrange(year, month)[1]
    if day + 7 > days_in_month:
        print("There might be a bug")
        if month > 11:
            print("theres might be a bug")
    for x in range(7):
        if day + x > days_in_month:
            print("uh oh there might be a bug")
            if month > 11:
                year += 1
                month = 1
                day = 1
            else:
                print("variables have been added to")
                month += 1
                day = 1
                bug_fix = x
                print(f"month is {month}")
                print(f"day is {day}")
        with open('calendar.json', 'r') as openfile:
            calendar = json.load(openfile)
        events = calendar[str(year)][str(month)][str(day + x - bug_fix)]
        for i in range(len(events)):
            return_list.append([events[str(i)]["Title"], events[str(i)]["Description"],
                                f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}", [], events[str(i)]["Priority"]])
            for y in range(len(events[str(i)]["People"])):
                return_list[i][3].append(events[str(i)]["People"][str(y)])
    return_str = f"You have {len(return_list)} events for that week: "
    for i in range(len(return_list)):
        temp_str = ""
        temp_str += f" #{i + 1} {return_list[i][0]} - {return_list[i][1]} with priority value {return_list[i][4]} at {return_list[i][2]} with {len(return_list[i][3])} people:"
        for y in range(len(return_list[i][3])):
            temp_str += f" {return_list[i][3][y]}"
        temp_str += "."
        return_str += temp_str
    return return_str
def make_event(day: int = 1, month: int = 4, year: int = 2024, description: str = "Testing - the description likely wasn't processed", title: str = "Error or testing", hour: int = 0, minutes: int = 0, people_associated: list = []) -> str:
    """Use this function to create an event

    Args:
        day (int): The day of the event
        month (int): The number of the month of the event
        year (int): The year of the event
        description (str): The description of the event to be added
        title (str): The title of the event to be added
        hour (int): The hour at the start time of the event
        minutes (int): The minutes at the start time of the event

    Returns:
        str: The date, title, and description of the event added
    """
    with open('calendar.json', 'r') as openfile:
        old_events = json.load(openfile)
    index = len(old_events[str(year)][str(month)][str(day)])
    event = {
        index: {
            "Title": title,
            "Description": description,
            "People": {},
            "Date": {
                "Year": year,
                "Month": month,
                "Day": day,
                "Hour": hour,
                "Minute": minutes
            }
        }
    }
    for i in range(len(people_associated)):
        event[index]["People"].update({str(i): people_associated[i]})
    old_events[str(year)][str(month)][str(day)].update(event)
    json_obj = json.dumps(old_events, indent=3)
    with open("calendar.json", "w") as outfile:
        outfile.write(json_obj)
    return f"Created an event on {int_to_str_months[month]} {day} {year} with the title: {title}, description: {description}, at {hour}:{minutes}"

recog = sr.Recognizer()
microphone = sr.Microphone()
print("listening...")
with microphone as source:
    audio = recog.listen(source)
prompt = recog.recognize_whisper(audio)
print(prompt)
assistant = Assistant(
    tools=[find_events, make_event, find_events_in_week],
    show_tool_calls=False,
    llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"),
    description="You are a secretary assistant who provides helpful and concise information about the user's calendar. If the user asks what is happening on a day, use find_events, but if they ask for a week, use find_events_in_week")
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



