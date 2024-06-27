
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}

def read_event(date):
    calendar_file = open("calendar.txt", "r")
    calendar_lines = calendar_file.readlines()
    events_file = open("events.txt", "r")
    events_lines = events_file.readlines()
    response_list = []
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
                print(f"Title: {cur_event_parsed[1][1:-1]} Description: {cur_event_parsed[2][1:-1]} Time: {cur_event_parsed[3][1:-1]}:{cur_event_parsed[4][1:-1]}")
                response_list.append([cur_event_parsed[1][1:-1], cur_event_parsed[2][1:-1]])
            else:
                print("Dates do not align. Something wrong has happened")
                print(f"The date of the event is {cur_event_parsed[0][1:-1]}")
        return response_list
    except:
        print("Something went wrong. Try deleting contents in calendar.txt and running cal.py")


print(read_event([4, 1, 2025]))

def read_events2(date):
    with open('events2.json', 'r') as openfile:
        calendar_file = json.load(openfile)
    events_file = open("events.txt", "r")
    events_lines = events_file.readlines()
    response_list = []
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
                print(f"Title: {cur_event_parsed[1][1:-1]} Description: {cur_event_parsed[2][1:-1]} Time: {cur_event_parsed[3][1:-1]}:{cur_event_parsed[4][1:-1]}")
                response_list.append([cur_event_parsed[1][1:-1], cur_event_parsed[2][1:-1]])
            else:
                print("Dates do not align. Something wrong has happened")
                print(f"The date of the event is {cur_event_parsed[0][1:-1]}")
        return response_list
    except:
        print("Something went wrong. Try deleting contents in calendar.txt and running cal.py")