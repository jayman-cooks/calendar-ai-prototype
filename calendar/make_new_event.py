#  date format mm/dd/yyyy
import json
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def make_new_event(title: str, description: str, date, hour: int, minutes: int):
    event_file = open("events.txt", "a")
    event_file.write(f"'{date}'_'{title}'_'{description}'_'{hour}'_'{minutes}'\n")
    event_file.close()
    event_file = open("events.txt", "r")
    index = len(event_file.readlines()) - 1
    event_file.close()
    calendar_file = open("calendar.txt", "r+")
    cal_file_lines = calendar_file.readlines()
    date_point = f"{int_to_str_months[date[0]]} {date[2]}\n"
    print(f"the line you want to put the date is {cal_file_lines.index(date_point) + date[1] +1}")

    cal_file_lines[cal_file_lines.index(date_point) + date[1]] = f"{cal_file_lines[cal_file_lines.index(date_point)+date[1]][:-2]} {index} \n"
    calendar_file.close()
    calendar_file = open("calendar.txt", "w")
    calendar_file.writelines(cal_file_lines)
    calendar_file.close()
    print(index)


def make_new_event2(title: str, description: str, date, hour: int, minutes: int):
    event = {
        {
            "Title": title,
            "Description": description,
            "Date": {
                "Year": date[2],
                "Month": date[0],
                "Day": date[1],
                "Hour": hour,
                "Minute": minutes
            }
        }
    }
    with open('calendar.json', 'r') as openfile:
        old_events = json.load(openfile)
    old_events[str(date[2])][str(date[0])][str(date[1])].update(event)
    json_obj = json.dumps(old_events, indent=3)
    with open("calendar.json", "w") as outfile:
        outfile.write(json_obj)


make_new_event2("Dinner", "Dinner with Joseph.", [4, 1, 2025], 17, 30)