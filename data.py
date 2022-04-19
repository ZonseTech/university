from itertools import count
from db import cursor, departments as d, instructors as i

sql = f"SELECT id, name, d.dept_name, salary FROM {i} i, {d} d where d.dept_name=i.dept_name"

cursor.execute(sql)
instructors = cursor.fetchall()

sql = f"SELECT dept_name, building, budget FROM {d}"
cursor.execute(sql)
departments = cursor.fetchall()
