from TODO import Task
from TODO import TodoList

Ironing = Task('Ironing')
# add instance of washing to the TodoList class
Washing = TodoList("Washing")
# add Washing to the TodoList
Washing.add_task("Washing")
# display the TodoList
Washing.display_tasks()
ironing = TodoList("Ironing")
ironing.add_task("Ironing")
ironing.display_tasks()