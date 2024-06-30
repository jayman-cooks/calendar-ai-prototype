#  date format mm/dd/yyyy
import json
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}





def make_new_event2(title: str, description: str, date, hour: int, minutes: int, people_associated: list = [], priority: int = 0):
    with open('calendar.json', 'r') as openfile:
        old_events = json.load(openfile)
    index = len(old_events[str(date[2])][str(date[0])][str(date[1])])
    event = {
        index: {
            "Title": title,
            "Description": description,
            "Priority": priority,
            "People": {},
            "Date": {
                "Year": date[2],
                "Month": date[0],
                "Day": date[1],
                "Hour": hour,
                "Minute": minutes
            }
        }
    }
    for i in range(len(people_associated)): # Adds all ppl to ppl list
        event[index]["People"].update({str(i): people_associated[i]})
    old_events[str(date[2])][str(date[0])][str(date[1])].update(event)
    json_obj = json.dumps(old_events, indent=3)
    with open("calendar.json", "w") as outfile:
        outfile.write(json_obj)


make_new_event2("Meeting", "Meeting with John.", [4, 1, 2025], 12, 30, ["John"], priority=1)