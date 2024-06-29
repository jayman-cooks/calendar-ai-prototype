import json
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def read_events2(date):
    with open('calendar.json', 'r') as openfile:
        calendar = json.load(openfile)
    year = date[2]
    month = date[0]
    day = date[1]
    events = calendar[str(year)][str(month)][str(day)]
    return_list = []
    for i in range(len(events)):
        return_list.append([events[str(i)]["Title"], events[str(i)]["Description"],
                            f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}", []])
        for x in range(len(events[str(i)]["People"])):
            return_list[i][3].append(events[str(i)]["People"][str(x)])
    print(return_list)
    print(f"here are all the events: {calendar[str(year)][str(month)][str(day)]}")
    return calendar[str(date[2])][str(date[0])][str(date[1])]


print(read_events2([4, 1, 2025]))