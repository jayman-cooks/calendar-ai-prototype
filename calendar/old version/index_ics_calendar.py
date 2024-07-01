def test_date(index):
    return f'{int_to_str_months[int(list_of_dates[index][4:6])]} {list_of_dates[index][:4]}\n' in out_cal_lines
def bin_search(list, start, end, x):
    if end >= start:

        mid = (end + start) // 2

        # If element is present at the middle itself
        if list[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif list[mid] > x:
            return bin_search(list, start, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return bin_search(list, mid + 1, end, x)

    else:
        # Element is not present in the array
        return -1

# input the path of the .ics file you wish to import
inp_cal_path = "/home/john/Downloads/pers_calendar.ics"
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}
inp_cal = open(inp_cal_path, "r")
inp_cal_lines = inp_cal.readlines()
counter = 0
for i in inp_cal_lines:
    if i == "BEGIN:VEVENT\n":
        counter += 1
vevent_start_indexes_list = [index for index, x in enumerate(inp_cal_lines) if x.startswith("BEGIN:VEVENT")]
vevent_end_indexes_list = [index for index, x in enumerate(inp_cal_lines) if x.startswith("END:VEVENT")]
final_list = []
for start, end in zip(vevent_start_indexes_list, vevent_end_indexes_list):
    final_list.append(inp_cal_lines[start:end + 1])
print(counter)
print(len(vevent_start_indexes_list))
print(len(vevent_end_indexes_list))
print(vevent_start_indexes_list)

print("______________")
print(final_list[0])
list_of_dates = []
for i in range(len(final_list)):
    list_of_dates.append(final_list[i][1][8:16])

print(list_of_dates)
calendar_file = open("calendar.txt", "r")
out_cal_lines = calendar_file.readlines()
control = f'April 2024\n' in out_cal_lines
test_month = test_date(0)
if not test_date(0):
    if test_date(len(list_of_dates)):
        print("not all dates in the calendar you wish to import are included in the output file. Truncating these events...")
        month_count_list = []
        for i in range(len(list_of_dates)):
            month_count_list.append(int(list_of_dates[i][:4]) * 12 + int(list_of_dates[i][4:6]))
        # Need to add code to take line 0 of out cal file into month count, find index of first matching using binary seaches

    else:
        print("none of the dates of the events you provided are in the output calendar. Ignoring...")
else:
    print("All dates of events provided are in the output file. Keeping original...")
