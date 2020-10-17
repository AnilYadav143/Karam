#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
</head>
<body>
<h1>Edit Profile From</h1>
<hr>
<form action="editcode.py" method="post">
<table>

"""
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
e=cgi.FieldStorage().getvalue('id')
cur=con.cursor()
q="select * from tbl_employee where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td><input name='name' value='"+r[1]+"'</td></tr>"
 print "<tr><td> Father Name :</td><td><input name='fname' value='"+r[2]+"'</td></tr>"
 m=""
 f=""
 if r[3]=="male":
  m="checked"
 if r[3]=="female":
  f="checked"
 print "<tr><td>Gender</td><td><input type='radio' name='gender' value='"+r[3]+"' "+m+"/>Male<input type='radio' name='gender' value='female' "+f+"/>Female</td></tr>"
 print "<tr><td>Mobile No:</td><td><input type='number' name='mobile' value='"+r[6]+"'</td></tr>"
 print "<tr><td>Email :</td><td><input name='email' value='"+r[4]+"' readonly /></td></tr>"
 print "<tr><td>Address :</td><td><input name='address' value='"+r[9]+"'/></td></tr>"
 print "<tr><td colspan='3' align='center'><input type='submit' value='update' /></td></tr>"
print """
</table>
</form>
</body>
</html>
"""











