#!/usr/bin/env python3

import sqlite3

tut_01 = False
tut_02 = False
tut_03 = True

def main():
  FILENAME = "ll.sqlite"
  tablename = "tablename"
  # instantiates instances of db interface
  db = sqlite3.connect(FILENAME)
  cur = db.cursor()


  if (tut_01):
    cur.execute("SELECT sqlite_version()")
    version = cur.fetchone()[0]
    print(f"SQLite3 version {version}")
  
  if (tut_02):
    # TODO: How to create tables given a table name?
    # TODO: How to create columns given table headers?

    # .execute does not return any values and only takes in SQL strings
    cur.execute("DROP TABLE IF EXISTS tablename")
    cur.execute("CREATE TABLE IF NOT EXISTS tablename (a TEXT, b TEXT, c TEXT)")
    cur.execute("INSERT INTO tablename VALUES ('one', 'two', 'three')")
    cur.execute("INSERT INTO tablename VALUES ('four', 'five', 'six')")
    cur.execute("INSERT INTO tablename VALUES ('seven', 'eight', 'nine')")
    db.commit()

    cur.execute("SELECT * FROM tablename")

    # -- cursor as interator
    # for row in cur:
    #   print(row)
    
    # -- fetchone
    # row = cur.fetchone()
    # while row:
    #   print(row)  
    #   row = cur.fetchone()

    # -- fetchall (need enough RAM to hold all data)
    rows = cur.fetchall()
    for row in rows:
      print(row)

  if (tut_03):
    note = "a prepared statement is a statement thats parsed once by the DB engine "
    note += "then used over and over w/ diff values"
    print(note)

    data = "('one', 'two', 'three')"
    drop_table_query = "DROP TABLE IF EXISTS " + tablename
    create_table_query = """CREATE TABLE IF NOT EXISTS """+ tablename +""" (a TEXT, b TEXT, c TEXT)"""
    insert_data_query = "INSERT INTO "+ tablename +" VALUES "+ data
    select_query = "SELECT * FROM "+ tablename

    cur.execute(drop_table_query)
    cur.execute(create_table_query)
    cur.execute(insert_data_query)
    db.commit()
    cur.execute(select_query)

    for row in cur:
      print(row)
    


  cur.execute("DROP TABLE IF EXISTS tablename")
  cur.close()
  db.close()



if __name__ == '__main__':
  main()
  #dont have mysql

