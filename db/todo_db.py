import sqlite3


def main():

  # init
  FILENAME = "todo.sqlite"

  # instantiates instances of db interface
  db = sqlite3.connect(FILENAME)
  cur = db.cursor()

  # create table
  cur.execute("DROP TABLE IF EXISTS tasks")

  # add headers to table
  cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER AUTOINCREMENT PRIMARY KEY, #auto increment 
    creation_date CURRENT_TIMESTAMP, 
    expected_completion_date DATETIME,
    completion_date DATETIME,
    priority INTEGER,
    severity INTEGER,
    title VARCHAR(40),
    description VARCHAR(100),
    parent INTEGER,
    type VARCHAR(10),
    status VARCHAR(10), 
    author VARCHAR(10) FOREIGN KEY,
    assignee VARCHAR(10) FOREIGN KEY,
    dependencies INTEGER
    )
    """)

  # add data to table
  data = "('one', 'two', 'three')"
  insert_data_query = "INSERT INTO "+ tablename +" VALUES "+ data
  db.commit()

  # view data from table
  db.commit()

  # remove data from table
  db.commit()

  # view data from table
  db.commit()
    

  
  cur.close()
  db.close()

if __name__ == '__main__':
  main()