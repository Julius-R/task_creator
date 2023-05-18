from taskList import TaskList
from helpers import choose_option, get_user_selection
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
        print("Hello, what is your name?")
        name = get_user_selection("str")
        return {"tasks": TaskList(), "user": name}


def save_progress(tasks, user):
    with open("tasks.json", "w") as task_file:
        task_file.write(json.dumps({"tasks": tasks.get_tasks(), "user": user}, indent=4, cls=MyEncoder))

    print("\nData Saved!")


def main():
    details = get_init_details()
    tasks, user = details.values()
    OPTIONS_LIST = ("View Tasks", "Add Task", "Edit Task", "Quit")
    print(f"\nHello {user}!")
    while True:
        match choose_option(OPTIONS_LIST):
            case 1:
                tasks.view_tasks()
            case 2:
                tasks.add_task_loop()
            case 3:
                tasks.edit_task()
            case 4:
                save_progress(tasks, user)
                break

    print("Loop has ended, goodbye!")


main()
