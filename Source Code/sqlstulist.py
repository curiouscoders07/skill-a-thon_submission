import sqlite3
import subprocess
from sqlite3 import Error


con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
def stlist():
    cur.execute('select name from student where mentor="Mentee"' )
    d=cur.fetchall()
    d1=[]
    for i in d:
        d1.append(i[0])
    return d1