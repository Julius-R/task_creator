class Task:
    def __init__(self, task, inProgress=False, isCompleted=False):
        self.task = task
        self.inProgress = inProgress
        self.isCompleted = isCompleted

    def get_task_name(self):
        return self.task

    def mark_completed(self):
        self.isCompleted = True

    def update_progress(self):
        self.inProgress = not self.inProgress

    def get_details(self):
        status = ""
        if self.isCompleted:
            status = "Completed"
        elif self.inProgress:
            status = "In Progress"
        else:
            status = "Not Started"

        print(f"""Task: {self.task} \nStatus: {status}""")
