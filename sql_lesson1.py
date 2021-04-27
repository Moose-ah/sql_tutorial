'''
**************** Steps to Connect to an SQLite3 Database *******************
1. Create a new folder in the documents folder and name it sql_tutorial
2. Create a Python file in the sql_tutorial folder and name it lesson_1.py
3. Copy the below code and paste it into your lesson_1.py file
4. In the create_connection function replace username with your own username
5. From the sql_tutorial folder type python3 lesson_1 to run the program
6. The Terminal will say; Connection to SQLite DB successful
'''

import sqlite3
from sqlite3 import Error

#connects to database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("/Users/moussandiaye/hidden_genius_/sql_tutorial/sm_app.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

execute_query(connection, create_users_table)

create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)
