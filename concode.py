#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
name=data.getvalue('n')
#print n
email=data.getvalue('e')
#print e
mobile=data.getvalue('mo')
#print mo
message=data.getvalue('m')
#print m
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
query="insert into contact(name,email,mobile_no,message) values ('"+name+"','"+email+"','"+mobile+"','"+message+"')"
cur=con.cursor()
a=cur.execute(query)
if a==1:
 print """
 <script>
 alert("message sent");window.location.href="contact.py";
 </script>
 """
else:
 print
 "<script> alert('message not sent');window.location.href='contact.py';</script>"
 
con.commit()
con.close()
