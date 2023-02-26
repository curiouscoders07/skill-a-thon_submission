import sqlite3
import subprocess
from sqlite3 import Error


con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS student(name text,username text PRIMARY KEY, password text, gender text,mentor text)")
    con.commit()

# sql_table(con)
def sql_insert(entities,pas):
    cursorObj.execute("select * from student")
    d=cursorObj.fetchall()
    print(d)
    for i in d:
        if(i[1] == entities[1]):
            print(i[1])
            print(entities[1])
            subprocess.call(['python', 'existt.py'])
            return False
        if (entities[2] not in pas):
            subprocess.call(['python', 'notmatch.py'])
            return False

    cursorObj.execute('INSERT INTO student(name, username, password, gender, mentor) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()
    subprocess.call(['python', 'crea.py'])
    return True

sql_table(con)
cursorObj.execute("select * from student")
d=cursorObj.fetchall()
print(d)