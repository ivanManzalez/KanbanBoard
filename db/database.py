#!/usr/bin/env python3
import sqlite3
import os

class Database:

  # CONSTRUCTOR
  def __init__(self, db_path):
    expanded_path = os.path.expanduser(db_path)
    self.db = sqlite3.connect(expanded_path)
    self.cur = self.db.cursor()

  # SQL VERSION
  def get_sqlversion(self):
    cur.execute("SELECT sqlite_version()")

  # CLOSE DB CONNECTION
  def close_db(self):
    self.cur.close()
    self.db.close()

  # ROLLBACK TO LAST COMMIT
  def rollback_db(self):
    self.cur.rollback()

  # COMMIT CHANGES TO DB
  def commit_db(self):
    self.cur.commit()

  # DELETE - TABLE
  def drop_table(self, tablename):
    self.cur.execute(f"DROP TABLE IF EXISTS {tablename}")
    return self.cur

  # DELETE - ENTITY
  def delete_entity_where(self, tablename, condition):
    delete_statement = f"DELETE FROM {tablename} WHERE {condition}"
    self.cur.execute(delete_statement)
    return self.cur

  # CREATE - TABLE
  def create_table(self, tablename, column_names, column_types):
    if(len(column_names) != len(column_types)):
      print("Length of column names != Length of column types")
      return None

    create_statement = f"CREATE TABLE IF NOT EXISTS {tablename} ("

    for col_name, col_type in zip(column_names, column_types):
      create_statement += f"{col_name} {col_type},"
    
    create_statement = create_statement[:-1] + ")"
    print("Create Statement:\n",create_statement)
    self.cur.execute(create_statement)
    return self.cur

  # CREATE - ENTITY
  def insert_data(self, tablename, data_tuple):
    insert_statement = f"INSERT INTO {tablename} VALUES {data_tuple}"
    self.cur.execute(insert_statement)
    return self.cur

  # CREATE - ENTITIES
  def insert_manydata(self, tablename, list_data_tuple):
    placeholders = "(?" + ", ?" * (len(list_data_tuple[0]) - 1) + ")"
    insert_statement = f"INSERT INTO {tablename} VALUES {placeholders}"
    self.cur.executemany(insert_statement, list_data_tuple)
    return self.cur

  # GET - COLUMNS
  def get_columns(self, tablename, column_names):
    select_statement = f"SELECT {', '.join(column_names)} FROM {tablename}"
    self.cur.execute(select_statement)
    return self.cur.fetchall()

  # GET - ALL COLUMNS
  def get_all_data(self, tablename):
    select_statement = f"SELECT * FROM {tablename}"
    self.cur.execute(select_statement)
    return self.cur.fetchall()

  # GET - ENTITY WHERE
  def get_data_where(self, tablename, condition):
    select_statement = f"SELECT * FROM {tablename} WHERE {condition}"
    self.cur.execute(select_statement)
    return self.cur.fetchall()

  # GET - COLUMNS WHERE
  def get_columns(self, tablename, column_names, condition):
    select_statement = f"SELECT {', '.join(column_names)} FROM {tablename} WHERE {condition}"
    self.cur.execute(select_statement)
    return self.cur.fetchall()
  
  # UPDATE - ENTITY FIELD
  def update_entity_field(self, tablename, field, new_value, condition):
    update_statement = f"UPDATE {tablename} SET {field} = {new_value} WHERE {condition}"
    self.cur.execute(update_statement)
    return self.cur
