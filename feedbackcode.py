#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Hello ji"
import cgi,MySQLdb
f=cgi.FieldStorage()
email=f.getvalue('email')
ftext=f.getvalue('ftext')
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
cur=con.cursor()
query="select name from tbl_employee where email='"+email+"'"
cur.execute(query)
res=cur.fetchall()
name=""
status="false"
for r in res:
 name=r[0]
 status="true"
q="insert into tbl_feedback(name,email,ftext,postdate) values ('"+name+"','"+email+"','"+ftext+"',sysdate())"
if status=="true":
 n=cur.execute(q)
 if n==1:
  print "<script>alert('feedback is successful submited');window.location.href='feedback.py'</script>"
 else:
  print "<script>alert('not feedback successful submited');window.location.href='feedback.py'</script>"
else:
 print "<script>alert('not feedback successful submited');window.location.href='feedback.py'</script>"
  
  
  
  