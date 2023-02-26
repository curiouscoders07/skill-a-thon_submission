import sqlite3

conn = sqlite3.connect('mydatabase.db')
cur = conn.cursor()

def checklogin(name,passw):
    cur.execute('select username,password from student')
    d=cur.fetchall()
    v=(name,passw)
    for i in d:
        if(v == i):
            cur.execute(f"select mentor from student where username='{i[0]}'")
            m = cur.fetchone()
            return m[0]

    return 0

