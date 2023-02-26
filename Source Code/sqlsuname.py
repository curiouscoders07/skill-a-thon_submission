import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()

def uname(a):
    cur.execute(f'select username from student where name ="{a}"')
    d=cur.fetchone()
    return d[0]
