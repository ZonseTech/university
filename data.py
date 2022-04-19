from db import cursor, departments as d, instructors as i

sql = f"SELECT id, name, d.dept_name, salary FROM {i} i, {d} d"

cursor.execute(sql)
instructors = cursor.fetchall()
