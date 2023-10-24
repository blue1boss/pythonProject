'''
sqlite-dml-insert.dy


SQL- insert 문
    INSERT INTO 테이블명 (컬럼명, 컬럼명....)
    VALUES (데이터, 데이터...)
'''

import sqlite3

conn= sqlite3. connect('hr.db')
cur = conn.cursor()

#SQL문 작성- 데이터 삽입
sql = "INSERT INTO employees" \
    "(first_name, last_name, email,"\
    "hire_date, job_id, salary, department_id)"\
    "VALUES (?, ?, ?, ?, ?, ?, ?)"

cur.execute(sql, ('John','Doe','Johndoe1@example.com',
                  '2023-07-15','IT_PROG', 5000,90))
'''
insert(삽입), update(수정), delete(삭제) 
commit 해주어야 db에 적용된다. 
'''


conn.commit()
cur.close()
conn.close()


