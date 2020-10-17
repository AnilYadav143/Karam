#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
refno=f.getvalue('refno')
ctext=f.getvalue('ctext')
con=MySQLdb.connect('127.0.0.1','root','','karam',3306)
cur=con.cursor()
query="insert into complain(name,mobileno,email,refno,ctext,sysdate) values('"+name+"','"+mobileno+"','"+email+"','"+refno+"','"+ctext+"',sysdate())"
n=cur.execute(query)
if n==1:
 print"<script>alert('Complain Succesfully Submitted');window.location.href='index.html';</script>"
else:
 print"<script>alert('Unsuccesfull Complain');window.location.href='complain.py';</script>"
 