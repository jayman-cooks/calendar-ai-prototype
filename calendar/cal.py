import calendar
import datetime
import time

years_out = 5
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}
date = str(datetime.date.today()).split("-")
year = int(date[0])
month = int(date[1])
print("month is " + str(month))
cal_file = open("calendar.txt", "a+")
cal_file.raw_str = cal_file.read()
date_not_split = str(datetime.date.today())
for i in range(month, 13):
    if i > 12:
        break
    print(i)
    cal_file.write(f"{int_to_str_months[i]} {year} {calendar.monthrange(year, i)[1]} days \n")
    for x in range(calendar.monthrange(year, i)[1]):
        cal_file.write(f"{str(x + 1)} \n")
for y in range(years_out - 1):
    for i in range(1, 13):
        if i > 12:
            break
        print(i)
        cal_file.write(f"{int_to_str_months[i]} {year + y} {calendar.monthrange(year + y, i)[1]} days \n")
        for x in range(calendar.monthrange(year + y, i)[1]):
            cal_file.write(f"{str(x + 1)} \n")