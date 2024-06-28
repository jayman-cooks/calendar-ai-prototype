import json
def find_events_in_week(day, month, year): # potential bug if week extends out of month
    return_list = []
    for x in range(7):
        with open('calendar.json', 'r') as openfile:
            calendar = json.load(openfile)
        events = calendar[str(year)][str(month)][str(day + x)]
        for i in range(len(events)):
            return_list.append([events[str(i)]["Title"], events[str(i)]["Description"],
                                f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}"])
    return_str = f"You have {len(return_list)} events for that week: "
    for i in range(len(return_list)):
        return_str += f"{i + 1}. {return_list[i][0]} - {return_list[i][1]} at {return_list[i][2]}"
    return return_str
print(find_events_in_week(1, 4, 2025))