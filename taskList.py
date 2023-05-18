from task import Task
from helpers import get_user_selection, choose_option
from typing import List


class TaskList:
    def __init__(self, tasks: List[Task] = []):
        self.tasks = []
        if len(tasks) > 0:
            for task in tasks:
                task, inProgress, isCompleted = task.values()
                self.tasks.append(Task(task, inProgress, isCompleted))

    def __add_task(self):
        print("\nEnter task details")
        task = get_user_selection("str")
        self.tasks.append(Task(task))

    def add_task_loop(self):
        while True:
            self.__add_task()
            print("\nTask added!\nDo you want to add another task? \nPress Enter for yes, or 'n' for no")
            user_selection = get_user_selection("str")
            if user_selection.lower() == "n":
                print("\nReturning to main menu! \n")
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
        user_selection = choose_option(self.tasks)
        return self.tasks[user_selection - 1]

    def edit_task(self):
        TASK_OPTIONS = ("Delete", "Start/Pause", "Mark Complete", "Cancel")
        task = self.__select_task()
        print("\nCurrently Editing:")
        task.get_details()
        print("\nOptions\n")
        user_selection = choose_option(TASK_OPTIONS)
        match user_selection:
            case 1:
                self.tasks.remove(task)
                print("\nTask Deleted! \n")
            case 2:
                task.update_progress()
                print("\nTask Progress Updated! \n")
            case 3:
                task.mark_completed()
                print("\nTask Marked Completed! \n")
            case 4:
                print("\nReturning to main menu! \n")
                return

    def get_tasks(self):
        return self.tasks
