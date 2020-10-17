#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
fname=f.getvalue('fname')
gender=f.getvalue('gender')
mobileno=f.getvalue('mobile')
email=f.getvalue('email')
address=f.getvalue('address')
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
q="update tbl_employee set name='"+name+"',fname='"+fname+"',gender='"+gender+"',m_number='"+mobileno+"',address='"+address+"' where email='"+email+"'"
cur=con.cursor()
cur.execute(q)
con.commit()
print "<script>window.location.href='eprofile.py?id="+email+"';</script>"
																													