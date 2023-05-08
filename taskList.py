from task import Task
from helpers import get_user_input_str, get_user_value_int
from typing import List


class TaskList:
    def __init__(self, tasks: List[Task] = []):
        self.tasks = []
        if len(tasks) > 0:
            for task in tasks:
                task, inProgress, isCompleted = task.values()
                self.tasks.append(Task(task, inProgress, isCompleted))

    def __add_task(self):
        task = get_user_input_str("\nEnter task details")
        self.tasks.append(Task(task))

    def add_task_loop(self):
        while True:
            self.__add_task()
            user_selection = get_user_input_str(
                "\nDo you want to add another task? \nPress Enter for yes, or 'n' for no"
            )
            if user_selection.lower() == "n":
                break

    def view_tasks(self):
        if len(self.tasks) < 1:
            print("\nThere are no tasks to display")
        else:
            print("\nTasks:")
            print("-" * 10)
            for task in self.tasks:
                task.get_details()
                print("-" * 10)

    def __select_task(self):
        print("Please select a task to edit \n")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1} - {task.get_task_name()}")
        user_selection = get_user_value_int()
        return self.tasks[user_selection]

    def edit_task(self):
        options = ("Delete", "Start", "Mark Complete")
        task = self.__select_task()
        print(f"Editing {task.get_task_name()}")
        print("Options")
        for index, option in enumerate(options):
            print(f"{index + 1} - {option}")
        user_selection = get_user_value_int()
        match user_selection:
            case 1:
                self.tasks.remove(task)
            case 2:
                task.update_progress()
            case 3:
                task.mark_completed()

    def get_tasks(self):
        return self.tasks
