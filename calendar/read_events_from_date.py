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
                            f"{events[str(i)]['Date']['Hour']}:{events[str(i)]['Date']['Minute']}", [], events[str(i)]["Priority"]])
        for y in range(len(events[str(i)]["People"])):
            return_list[i][3].append(events[str(i)]["People"][str(y)])
    print(return_list)
    print(f"here are all the events: {calendar[str(year)][str(month)][str(day)]}")
    return_str = f"You have {len(return_list)} events for that day:"
    for i in range(len(return_list)):
        temp_str = ""
        temp_str += f" #{i + 1} {return_list[i][0]} - {return_list[i][1]} with priority value {return_list[i][4]} at {return_list[i][2]} with {len(return_list[i][3])} people:"
        for y in range(len(return_list[i][3])):
            temp_str += f" {return_list[i][3][y]}"
        temp_str += "."
        return_str += temp_str
    return return_str


print(read_events2([4, 1, 2025]))