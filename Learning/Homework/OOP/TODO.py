class Task:
    def __init__(self, description):
        self.get_description = description
        self.is_completed = False
        self.mark_as_completed = self.is_completed = True


class TodoList:

    def __init__(self, task):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print(self.tasks)

    def mark_task_as_complete(self, task_index):
        pass