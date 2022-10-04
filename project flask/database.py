from atexit import register
from select import select
import pymysql as p
def getconnection():
    return p.connect(host="localhost",user="root",password="",database="rutik")
def addata(t):
    con=getconnection()
    cur=con.cursor()
    query1="insert into info(name,password,email,city)values(%s,%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

def fetchdata():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from info")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificdata(id):
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from info where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updatedata(t):
    con=getconnection()                  
    cur=con.cursor()
    query="update info set name=%s,password=%s,city=%s,email=%s where id=%s"
    cur.execute(query,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getconnection()                  
    cur=con.cursor()
    query="delete from info where id=%s"
    cur.execute(query,(id,))
    con.commit()
    con.close()   