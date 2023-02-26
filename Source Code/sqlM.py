import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
l=[]
def Mname():

    cur.execute('select * from student')
    d=cur.fetchall()
    for i in d:
        if i[4]=='Mentor':
            l.append(i[0])
    return l

