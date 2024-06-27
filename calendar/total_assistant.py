

import json
import httpx

from phi.assistant import Assistant
from phi.llm.ollama import Hermes
import speech_recognition as sr
import os
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def find_event(day: int = 1, month: int = 4, year: int = 2024) -> str:
    """Use this function to find current events

    Args:
        day (int): The day of the event
        month (int): The number of the month of the event
        year (int): The year of the event

    Returns:
        str: The descriptions and titles of the events.
    """
    date = [month, day, year]
    print(date)
    calendar_file = open("calendar.txt", "r")
    calendar_lines = calendar_file.readlines()
    events_file = open("events.txt", "r")
    events_lines = events_file.readlines()
    response_list = ""
    try:
        date_point = calendar_lines.index(f"{int_to_str_months[date[0]]} {date[2]}\n") + date[1]
        targ_day_parsed = calendar_lines[date_point].split(" ")[1:-1]
        event_count = len(targ_day_parsed)
        print(f"There are {event_count} event(s) that day.")
        for i in range(event_count):
            cur_event_parsed = events_lines[int(targ_day_parsed[i])][:-1].split("_")
            print(cur_event_parsed)
            if cur_event_parsed[0][1:-1] == str(date):
                print("Dates align. Proceeding..")
                print(f" Data for event {i}: Title: {cur_event_parsed[1][1:-1]}, Description: {cur_event_parsed[2][1:-1]} Time: {cur_event_parsed[3][1:-1]}:{cur_event_parsed[4][1:-1]}")
                response_list += f" Data for event {i}: Title: {cur_event_parsed[1][1:-1]}, Description: {cur_event_parsed[2][1:-1]} Time: {cur_event_parsed[3][1:-1]}:{cur_event_parsed[4][1:-1]}"
            else:
                print("Dates do not align. Something wrong has happened")
                print(f"The date of the event is {cur_event_parsed[0][1:-1]}")
        return response_list
    except:
        print("Something went wrong. Try deleting contents in calendar.txt and running cal.py")


def make_event(day: int = 1, month: int = 4, year: int = 2024, description: str = "Testing - the description likely wasn't processed", title: str = "Error or testing", hour: int = 0, minutes: int = 0) -> str:
    """Use this function to find current events

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
    date = [month, day, year]
    print(date)
    event_file = open("events.txt", "a")
    event_file.write(f"'{date}'_'{title}'_'{description}'_'{hour}'_'{minutes}'\n")
    event_file.close()
    event_file = open("events.txt", "r")
    index = len(event_file.readlines()) - 1
    event_file.close()
    calendar_file = open("calendar.txt", "r+")
    cal_file_lines = calendar_file.readlines()
    date_point = f"{int_to_str_months[date[0]]} {date[2]}\n"
    print(f"the line you want to put the date is {cal_file_lines.index(date_point) + date[1] + 1}")

    cal_file_lines[cal_file_lines.index(date_point) + date[
        1]] = f"{cal_file_lines[cal_file_lines.index(date_point) + date[1]][:-2]} {index} \n"
    calendar_file.close()
    calendar_file = open("calendar.txt", "w")
    calendar_file.writelines(cal_file_lines)
    calendar_file.close()
    print(index)
    return f"created an event titled {title}, with description: {description}, on  {int_to_str_months[month]}, {day}. {year}"


recog = sr.Recognizer()
microphone = sr.Microphone()
print("listening...")
with microphone as source:
    audio = recog.listen(source)
prompt = recog.recognize_sphinx(audio)
print(prompt)
assistant = Assistant(
    tools=[find_event, make_event],
    show_tool_calls=True,
    llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"),
    description="You are a secretary assistant who provides helpful and concise information about the user's calendar")
#show me whats happening on 1, 4, 2025
response = assistant.run(prompt, stream=False)
print("Below is the response:")
print(response)


print(response.split(")")[1])
translation_table = dict.fromkeys(map(ord, '\n'), None)
tts_line = response.split(")")[1].translate(translation_table)
print(tts_line)
print(f"echo '{tts_line}' | piper --model en_US-lessac-medium.onnx --output-raw | aplay -r 22050 -f S16_LE -t raw -")
#os.system("echo 'Welcome to the world of speech synthesis!' | piper --model en_US-lessac-medium --output_file welcome.wav") -- downloads model

os.system(f"echo '{tts_line}' | piper --model en_US-lessac-medium.onnx --output-raw | aplay -r 22050 -f S16_LE -t raw -")



