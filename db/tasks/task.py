class Task:

  def __init__(self, task_id, creation_datetime, completion_date, title,  description, status, task_type, urgency, importance, severity, priority):
    self.task_id = task_id
    self.creation_datetime = creation_datetime
    self.completion_date = completion_date
    self.title = title
    self.description = description
    self.status = status
    self.task_type = task_type
    self.urgency = urgency
    self.importance = importance
    self.severity = severity
    self.priority = priority