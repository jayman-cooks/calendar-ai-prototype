#  date format mm/dd/yyyy
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def make_new_event(title: str, description: str, date):
    event_file = open("events.txt", "a")
    event_file.write(f"'{date}'_'{title}'_'{description}'\n")
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


make_new_event("testing", "I am testing if this works", [4, 1, 2025])