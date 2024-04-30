from phi.assistant import Assistant
from phi.llm.ollama import Hermes
#  date format mm/dd/yyyy
int_to_str_months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}


def make_event(day: int = 1, month: int = 4, year: int = 2024, description: str = "Testing - the description likely wasn't processed", title: str = "Error or testing") -> str:
    """Use this function to find current events

    Args:
        day (int): The day of the event
        month (int): The number of the month of the event
        year (int): The year of the event
        description (str): The description of the event to be added
        title (str): The title of the event to be added

    Returns:
        str: The date, title, and description of the event added
    """
    date = [month, day, year]
    print(date)
    event_file = open("events.txt", "a")
    event_file.write(f"'{date}'_'{title}'_'{description}'\n")
    event_file.close()
    event_file = open("events.txt", "r")
    index = len(event_file.readlines()) - 1
    event_file.close()
    calendar_file = open("calendar.txt", "r+")
    cal_file_lines = calendar_file.readlines()
    date_point = f"{int_to_str_months[date[0]]} {date[2]}\n"
    print(f"the line you want to put the date is {cal_file_lines.index(date_point) + date[1] + 1}")

    cal_file_lines[cal_file_lines.index(date_point) + date[
        1]] = f"{cal_file_lines[cal_file_lines.index(date_point) + date[1]][:-2]} {index} \n"
    calendar_file.close()
    calendar_file = open("calendar.txt", "w")
    calendar_file.writelines(cal_file_lines)
    calendar_file.close()
    print(index)
    return f"created an event titled {title}, with description: {description}, on  {int_to_str_months[month]}, {day}. {year}"


assistant = Assistant(tools=[make_event], show_tool_calls=True, llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"))
assistant.print_response("Make an event on 1, 4, 2025 with the title doctor's appointment, with the description of appointment with Dr Young at 3")