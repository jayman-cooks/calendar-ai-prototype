import calendar
import datetime
from read_events_from_date import read_event
import time
# WARNING: Do not edit calendar.txt
years_out = 5
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}
date = str(datetime.date.today()).split("-")
year = int(date[0])
month = int(date[1])
cal_file_check = open("calendar.txt", "r")
cal_file_check.lines = cal_file_check.readlines()
if f"April {str(year + years_out - 2)}\n" in cal_file_check.lines:
    print("file already created, keeping original")
else:
    print("creating and writing to file...")
    cal_file = open("calendar.txt", "a+")
    cal_file.raw_str = cal_file.read()
    print(f"the file is {cal_file.raw_str} end of file")
    date_not_split = str(datetime.date.today())
    for i in range(month, 13):
        if i > 12:
            break
        cal_file.write(f"{int_to_str_months[i]} {year}\n")
        for x in range(calendar.monthrange(year, i)[1]):
            cal_file.write(f"{str(x + 1)} \n")
    for y in range(1, years_out - 1):
        for i in range(1, 13):
            if i > 12:
                break
            cal_file.write(f"{int_to_str_months[i]} {year + y}\n")
            for x in range(calendar.monthrange(year + y, i)[1]):
                cal_file.write(f"{str(x + 1)} \n")
    print("file finished")
    cal_file.close()
print(read_event([4, 1, 2025]))
