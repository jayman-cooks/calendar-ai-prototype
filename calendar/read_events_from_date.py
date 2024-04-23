int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}

def read_event(date):
    calendar_file = open("calendar.txt", "r")
    calendar_lines = calendar_file.readlines()
    events_file = open("events.txt", "r")
    events_lines = events_file.readlines()
    try:
        date_point = calendar_lines.index(f"{int_to_str_months[date[0]]} {date[2]}\n") + date[1]
        print(date_point)
        print(calendar_lines[date_point])
    except:
        print("Something went wrong. Try deleting contents in calendar.txt and running cal.py")



read_event([4, 1, 2025])