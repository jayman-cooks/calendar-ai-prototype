import json
import calendar as calp
def find_events_in_week(day, month, year): # potential bug if week extends out of month
    return_list = []
    bug_fix = 0 # to fix a bug that prevented it from searching correct days for month overflow
    days_in_month = calp.monthrange(year, month)[1]
    if day + 7 > days_in_month:
        print("There might be a bug")
        if month > 11:
            print("theres might be a bug")
    for x in range(7):
        if day + x > days_in_month:
            print("uh oh there might be a bug")
            if month > 11:
                year += 1
                month = 1
                day = 1
            else:
                print("variables have been added to")
                month += 1
                day = 1
                bug_fix = x
                print(f"month is {month}")
                print(f"day is {day}")
        with open('calendar.json', 'r') as openfile:
            calendar = json.load(openfile)
        events = calendar[str(year)][str(month)][str(day + x - bug_fix)]
        for i in range(len(events)):
            return_list.append([events[str(i)]["Title"], events[str(i)]["Description"],
                                f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}", [], events[str(i)]["Priority"]])
            for y in range(len(events[str(i)]["People"])):
                return_list[i][3].append(events[str(i)]["People"][str(y)])
    return_str = f"You have {len(return_list)} events for that week: "
    for i in range(len(return_list)):
        temp_str = ""
        temp_str += f" #{i + 1} {return_list[i][0]} - {return_list[i][1]} with priority value {return_list[i][4]} at {return_list[i][2]} with {len(return_list[i][3])} people:"
        for y in range(len(return_list[i][3])):
            temp_str += f" {return_list[i][3][y]}"
        temp_str += "."
        return_str += temp_str
    return return_str
print(find_events_in_week(1, 4, 2025))