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
