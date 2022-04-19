from db import cursor, instructors, connection


def save(params):
    sql = f"INSERT INTO {instructors}(name, dept_name, salary) VALUES(?, ?, ?)"
    cursor.execute(sql, params)
    connection.commit()

    return cursor
