from db.tasks_table import TasksTable
from db.utils import db_tuple_to_dict, get_datetime

################################################################

class Data:

  def __init__(self):
    self.tasks = TasksTable()
    self.user = "Manzalez98"

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.tasks.close_db()


  def get_tasks(self, task_status):
    print("\n",type(self).__name__,self.get_tasks.__name__)
    ret = []
    VALID_TASKS = ["To Do", "Completed", "In Progress"]
    
    if(task_status in VALID_TASKS):
      task_records = self.tasks.get_task_by_status(status_type=task_status)
      print(len(task_records))
      for task in task_records:
        ret.append( db_tuple_to_dict(self.tasks.column_names, task) )
    return ret

  def get_all(self):
    print("\n",type(self).__name__,self.get_all.__name__)
    ret = []
    task_tuples = self.tasks.get_all_tasks()
    for task_tuple in task_tuples:
      ret.append( db_tuple_to_dict(self.tasks.column_names, task_tuple) )
    return ret


  def create_new_task(self, task):
    print("\n",type(self).__name__,self.create_new_task.__name__)
    try:
      print("New task:", task)

      data = self.tasks.create_task( 
        title = task["title"], 
        description = task["description"], 
        urgency = task["urgency"], 
        importance=task["importance"], 
        creation_datetime=get_datetime, 
        completion_date = None, 
        status=task["status"], 
        task_type="Task", 
        severity=None, 
        priority=None, 
        dependents=None, 
        parents=None
      )
      return {
          "message":"New Task Created",
          "status":200,
          "data":data
        }

    except Exception as exp:
      return {
        "message":"Error when creating task", 
        "error":exp,
        "status":500,
        }
    
  def update_existing_task(self, task):
    print("\n",type(self).__name__,self.update_existing_task.__name__)
    try:
      print("Update task:", task)
      data = self.tasks.update_by_taskid(
        task=task, 
        task_id=task["task_id"],
      )
      return {
          "message":"Task Updated",
          "status":200,
          "data":data
        }

    except Exception as exp:
      return {
        "message":"Error when updating task", 
        "error":exp,
        "status":500,
        }

  def delete_existing_task(self, task_id):
    print("\n",type(self).__name__,self.delete_existing_task.__name__)
    try:

      data = self.tasks.delete_task_by_id(
        task_id=task_id,
      )
      return {
          "message":"Task deleted",
          "status":200,
          "data":data
        }

    except Exception as exp:
      return {
        "message":"Error when updating task", 
        "error":exp,
        "status":500,
        }


