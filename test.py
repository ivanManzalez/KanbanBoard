from data import Data

db_data = Data()

task = {
  "title":"Task Title",
  "description":"Task description",
  "urgency":"Urgent",
  "importance":"Importance",
  }
 
new_task = db_data.create_new_task(task)

print(new_task)


all_tasks = db_data.get_all()
print(all_tasks)