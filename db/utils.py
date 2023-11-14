from datetime import datetime

def get_datetime(formatted = "%Y-%m-%d %H:%M:%S"):
  return datetime.now().strftime(formatted)

def db_tuple_to_dict(column_names, data_tuple):
  return {column_names[i]: data_tuple[i] for i in range(len(column_names))}