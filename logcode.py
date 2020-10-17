#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "logcode"
import cgi,MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
p=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
query="select * from tbl_employee where email='"+e+"' and password='"+p+"'"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
if a==1:
 print "<script>window.location.href='eprofile.py?id="+e+"';</script>"
else:
 print "<script>window.location.href='login.py'</script>"				