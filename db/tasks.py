from db.database import Database

class Singleton(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

class TasksTable(metaclass=Singleton):
  # Initialize Database object
  DB_PATH = "db/todo.sqlite"

  def __init__(self, db_path = DB_PATH):
    self.TABLENAME = "tasks"
    self.db = Database(db_path)
    self.column_types = [
      "INTEGER PRIMARY KEY AUTOINCREMENT",# task_id
      "CURRENT_TIMESTAMP",                # creation_date
      "DATE NULL",                        # completion_date
      "VARCHAR(40)",                      # title
      "VARCHAR(255)",                     # description
      "VARCHAR(10)",                      # status
      "VARCHAR(10)",                      # task_type
      "VARCHAR(15)",                      # urgency
      "VARCHAR(15)",                      # importance
      "INTEGER NULL",                     # severity
      "INTEGER NULL",                     # priority
      "INTEGER NULL",                     # subtask_id
      # "REFERENCES tasks(task_id)",        # FOREIGN KEY (subtask_id)
      "INTEGER NULL",                     # supertask_id
      # "REFERENCES tasks(task_id)",        # FOREIGN KEY (supertask_id)
      ]
    self.column_names = [
      "task_id",                    # INTEGER PRIMARY KEY AUTOINCREMENT
      "creation_date",              # CURRENT_TIMESTAMP
      "completion_date",            # DATE NULL
      "title",                      # VARCHAR(40)
      "description",                # VARCHAR(255)
      "status",                     # VARCHAR(10)
      "task_type",                  # VARCHAR(10)
      "urgency",                    # VARCHAR(10)
      "importance",                 # VARCHAR(10)
      "severity",                   # INTEGER NULL
      "priority",                   # INTEGER NULL
      "subtask_id",                 # INTEGER NULL
      # "FOREIGN KEY (subtask_id)",   # REFERENCES tasks(task_id)
      "supertask_id",               # INTEGER NULL
      # "FOREIGN KEY (supertask_id)", # REFERENCES tasks(task_id)
      ]
    self.db.drop_table(tablename=self.TABLENAME)
    self.db.create_table(tablename=self.TABLENAME, column_names= self.column_names, column_types= self.column_types)

  # Create Task
  def create_task(self, title, description, urgency, importance, completion_date = None, status="To Do", task_type="Task", severity=None, priority=None, dependents=None, parents=None):
    data_tuple = (None, None, completion_date, title, description, status, task_type, urgency, importance, severity, priority, dependents, parents) #list of tuples for multi tasks
    return self.db.insert_data(tablename=self.TABLENAME, data_tuple=data_tuple)
    # return self.db.insert_manydata(tablename=self.TABLENAME, list_data_tuple=data_tuple)

  # Retrieve Task
  def get_task_by_id(self, task_id):
    condition = f"task_id = {task_id}"
    return self.db.get_data_where(tablename=self.TABLENAME, condition=condition)

  def get_task_by_status(self, status_type):
    condition = f"status = {status_type}"
    return self.db.get_data_where(tablename=self.TABLENAME, condition=condition)

  # Delete Task
  def delete_task_by_id(self, task_id):
    condition = f"task_id = {task_id}"
    self.db.delete_entity_where(tablename=self.TABLENAME, condition=condition)

  # Update Task
  def update_by_taskid(self, task_id, col_name, new_value):
    condition = condition = f"task_id = {task_id}"
    return self.db.update_entity_field(tablename=self.TABLENAME, field=col_name, new_value=new_value, condition=condition)
