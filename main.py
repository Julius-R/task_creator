from taskList import TaskList
from helpers import choose_option, get_user_input_str
import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def get_init_details():
    try:
        with open("tasks.json", "r") as task_file:
            details = json.load(task_file)
            tasks, user = details.values()
            print(tasks)
            return {"tasks": TaskList(tasks), "user": user}
    except FileNotFoundError:
        return {"tasks": TaskList(), "user": get_user_input_str("Enter your name")}


def save_progress(tasks, user):
    with open("tasks.json", "w") as task_file:
        task_file.write(json.dumps({"tasks": tasks.get_tasks(), "user": user}, indent=4, cls=MyEncoder))

    print("\nData Saved!")


def main():
    details = get_init_details()
    tasks, user = details.values()
    print(f"\nHello {user}!")
    while True:
        try:
            print("\nWhat would you like to do?")
            user_choice = choose_option()
        except:
            print("Some error occured")
        match user_choice:
            case 1:
                tasks.view_tasks()
            case 2:
                tasks.add_task_loop()
            case 3:
                tasks.edit_task()
            case 4:
                save_progress(tasks, user)
                break
    print("Loop has ended!")


main()
