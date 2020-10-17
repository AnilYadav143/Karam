#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "pagal"
print """
<html>
<head>
</head>
<body>
<h1>Employee Profile</h1>
<hr>
<table>
"""
import cgi,MySQLdb
e=cgi.FieldStorage().getvalue('id')
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
cur=con.cursor()
q="select * from tbl_employee where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td>",r[1],"</td></tr>"
 print "<tr><td>Father Name :</td><td>",r[2],"</td></tr>"
 print "<tr><td>Gender :</td><td>",r[3],"</td></tr>"
 print "<tr><td>Email :</td><td>",r[4],"</td></tr>"
 print "<tr><td>password :</td><td>",r[5],"</td></tr>"
 print "<tr><td>Mobile No :</td><td>",r[6],"</td></tr>"
 print "<tr><td>Address :</td><td>",r[9],"</td></tr>"
 
 print "<tr><td>Res.date :</td><td>",r[11],"</td></tr>"
 print "<tr><td colspan="2" align='center'><a  href='edit.py?id="+e+"'>Edit Profile</a></td></tr>"
 
print"""
</table>
</body>
</html>
"""