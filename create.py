import sqlite3

"""
Defining variables
"""
# database name
schema = "university"
# database file name
database_name = f"{schema}.db"

# database table names
departments = "department"  # stores db departments
instructors = "instructors"  # stores db instructors

# creating a connection to the database
# sqlite3 object will make connection and
# create database schema with the filename
# {{ university.db }}
connection = sqlite3.connect(database_name)

# database exception handling
with connection:
    # create a cursor object
    cursor = connection.cursor()

# sql statements to create tables
sql = [
    f"CREATE TABLE IF NOT EXISTS {departments} (dept_name TEXT PRIMARY KEY, building TEXT, budget NUMERIC)",
    f"CREATE TABLE IF NOT EXISTS {instructors} ("
    f"ID INTEGER PRIMARY KEY AUTOINCREMENT, "
    f"name TEXT,"
    f"dept_name TEXT,"
    f"salary NUMERIC,"
    f"FOREIGN KEY(dept_name) REFERENCES {departments}(dept_name))",
]

try:
    # looping though sql statements
    for stm in sql:
        # execute SQL query
        cursor.execute(stm)
except Exception as error:
    print(error)
