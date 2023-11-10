from db.tasks import TasksTable

################################################################

class Data():
    first_header = "world"
    second_header = "second"

################################################################
"""
  title = "New Task 1", 
  description = "The description for task 1", 
  urgency = "Urgent", 
  importance = "Not Important", 
  completion_date = None, 
  status="To Do", 
  task_type="Task", 
  severity=None, 
  priority=None, 
  dependents=None, 
  parents=None
"""
tasks = TasksTable()

for i in range(10):
  tasks.create_task(
    title = f"New Task {i}", 
    description = f"The description for task {i}", 
    urgency = "Urgent", 
    importance = "Not Important", 
    )

for i in range(10):
  rows = tasks.get_task_by_id(task_id=i)
  for row in rows:
    print(row)

for i in range(10):
  tasks.update_taskid_field(task_id=i, col_name="urgency", new_value="not Urgent")

for i in range(10):
  rows = tasks.get_task_by_id(task_id=i)
  for row in rows:
    print(row)

for i in range(10):
  tasks.delete_task_by_id(task_id=i)

for i in range(10):
  rows = tasks.get_task_by_id(task_id=i)
  for row in rows:
    print(row)
