

import json
import httpx

from phi.assistant import Assistant
from phi.llm.ollama import Hermes
import speech_recognition as sr
import os
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
        return_list.append([events[str(i)]["Title"], events[str(i)]["Description"], f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}"])
    print(return_list)
    print(f"here are all the events: {calendar[str(year)][str(month)][str(day)]}")
    #return calendar[str(date[2])][str(date[0])][str(date[1])]
    return_str = f"You have {len(return_list)} events for that day: "
    for i in range(len(return_list)):
        return_str += f"{i + 1}. {return_list[i][0]} - {return_list[i][1]} at {return_list[i][2]}"
    return return_str


def make_event(day: int = 1, month: int = 4, year: int = 2024, description: str = "Testing - the description likely wasn't processed", title: str = "Error or testing", hour: int = 0, minutes: int = 0) -> str:
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
            "Date": {
                "Year": year,
                "Month": month,
                "Day": day,
                "Hour": hour,
                "Minute": minutes
            }
        }
    }
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
prompt = recog.recognize_sphinx(audio)
print(prompt)
assistant = Assistant(
    tools=[find_events, make_event],
    show_tool_calls=False,
    llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"),
    description="You are a secretary assistant who provides helpful and concise information about the user's calendar. If the user asks what is happening on a day, use find_events")
#show me whats happening on 1, 4, 2025
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



