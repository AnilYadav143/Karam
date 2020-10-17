#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
title=data.getvalue('title')

salary=data.getvalue('salary')

exp=data.getvalue('exp')

loc=data.getvalue('location')
con=MySQLdb.connect('127.0.0.1','root','','karam',3306)
cur=con.cursor()
q="insert into tbl_job(title,salary,experience,Location,date) values ('"+title+"','"+salary+"','"+exp+"','"+loc+"',sysdate())" 
n=cur.execute(q)
if n==1:
 print "<script>alert('success');window.location.href='job.py';</script>"
else:
 print "<script>alert('Unsuccess');window.location.href='job.py';</script>"