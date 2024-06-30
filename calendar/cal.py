import calendar
import datetime
#from read_events_from_date import read_event
import json
import time
# WARNING: Do not edit calendar.txt
years_out = 5
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def gen_cal2():
    years_out = 5
    date = str(datetime.date.today()).split("-")
    year = int(date[0])
    month = int(date[1])
    years = {}
    for i in range(years_out):
        years.update({
            str(year + i): {

            }
        })
    for i in range(years_out):
        for x in range(12):
            years[str(year + i)].update({
                str(x + 1): {}
            })
            for y in range(calendar.monthrange(year + i, x + 1)[1]):
                years[str(year + i)][str(x + 1)].update({
                    str(y + 1): {}
                })
    json_obj = json.dumps(years, indent=3)
    with open("calendar.json", "w") as outfile:
        outfile.write(json_obj)
gen_cal2()