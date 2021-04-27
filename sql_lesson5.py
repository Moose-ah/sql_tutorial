'''
****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Baba                                                           *
*  Date     March 16, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************
'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


##################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("/Users/moussandiaye/hidden_genius_/sql_tutorial/oak8_pods.sqlite5")


##################  Create staff table variable query ################
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

################# Create pod leader query ################
create_pod_leader_table_query = """
CREATE TABLE IF NOT EXISTS pod_leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

################# Create pod member query ################
create_pod_member_table_query = """
CREATE TABLE IF NOT EXISTS pod_member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

################ Executive query to create _____ table #################
execute_query(connection, create_staff_member_table_query) 

execute_query(connection, create_pod_leader_table_query)

execute_query(connection, create_pod_member_table_query)


################## Create insert query to add _____ members to _____ table #######
add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""


add_pod_leader_query = """
INSERT INTO
    pod_leader (name,cell, position)
VALUES
    ('Jacore','1234567','Pod Leader')
"""


add_pod_member_query = """
INSERT INTO
    pod_member (name,cell, position)
VALUES
    ('Moussa','54637829','Pod Member')
"""

#################  Execute insert _____ members query ##################
execute_query(connection, add_staff_members_query)

execute_query(connection, add_pod_leader_query)

execute_query(connection, add_pod_member_query)


################# Display staff_member Query ##################### 
display_staff_query = "SELECT * from staff"
staff = execute_read_query(connection, display_staff_query)

for user in staff:
  print(user)

execute_query(connection,'drop table staff')

################# Display pod_leader Query ##################### 
display_pod_leader_query = "SELECT * from pod_leader"
pod_leader = execute_read_query(connection, display_pod_leader_query)

for user in pod_leader:
  print(user)

execute_query(connection,'drop table pod_leader')

################# Display pod_member Query ##################### 
display_pod_member_query = "SELECT * from pod_member"
pod_member = execute_read_query(connection, display_pod_member_query)

for user in pod_member:
  print(user)

execute_query(connection,'drop table pod_member')
