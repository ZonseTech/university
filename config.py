from db import cursor, departments, instructors, connection

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

    # Commit the changes
    connection.commit()

    # Close our connection
    connection.close()

except Exception as error:
    print(error)
