#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "show all complain"
import MySQLdb
print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="../css/job.css">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="../css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
<script src="../js/jquery-2.1.0.min.js"></script>
<script src="../js/bootstrap.min.js"></script>

<style>
#job{
	height:400px;
	width:100%;
	background-color:lightgrey;
	margin-top:-18px;
	background-image:url('images/back.png');
	background-size:100% 100%;
}
#job h1{
	padding-top:5%;
	color:red;
	font-size:50px;
	font-family:calbria;
	font-weight:bold;

}
th{
	color:blue;
}
td{

}
</style>
</head>
<body>
<div class="outer">
<div class="header">
<img src="../images/32.jpeg" id="image2"/>
</div>

<!--menubar starts here-->
<nav class="navbar navbar-inverse" style="margin-bottom:0px";>
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="employee.py">Add Employee</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="viewemployee.py">View Employee</a></li>
        <li><a href="notification.py">Add Notification</a></li>
		<li><a href="complain.py">View Complain</a></li>
		<li><a href="contact.py">View Contactus</a></li>
        <li><a href="adminfeedback.py">View Feedback</a></li>
		 <li><a href="job.py">Add Jobs</a></li>
            <li><a href="adminlogout.py">Log Out</a></li>
           
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <form class="navbar-form navbar-left" role="search">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      </ul>
    </div>
	<!-- /.navbar-collapse -->
  </div>
  <!-- /.container-fluid -->
</nav>
<!--menubar ends here-->


<!-- job show ..... -->
<div id="job" align="center">
		<h1 align="center">All Jobs</h1>
	<table border="1">
	<tr>
		<th>ID</th>
		<th>Title</th>
		<th>Salary</th>
		<th>Experience</th>
		<th>Location</th>
		<th>Date</th>
	</tr>
	"""
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","karam",3306)
query="select * from tbl_job"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
for row in res:
 print "<tr>"
 print "<td>",row[0],"</td>"
 print "<td>",row[1],"</td>"
 print "<td>",row[2],"</td>"
 print "<td>",row[3],"</td>"
 print "<td>",row[4],"</td>"
 print "<td>",row[5],"</td>"
print "</tr>"
print """
</table>
</div>
	<!-- job show end..... -->
<!--Footer start here-->
<div class="d-flex" style="min-height:100px;background-color:rgba(63,79,89,0.5);color:black;width:100%;">
<div class="col-sm-4">
<h3>Copyright &copy; KARAM INDUSTRY</h3>
</div>
<div class="col-sm-4" style="margin-top: 20px;">
<a href="www.facebook.com"><span class="fa fa-facebook fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.twitter.com"><span class="fa fa-twitter fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.instagram.com"><span class="fa fa-instagram fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.youtube.com" style="color:darkred;"><span class="fa fa-youtube fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.user.com"><span class="fa fa-user fa-3x"></span></a>
</div>
<div class="col-sm-4">
<h1 style="color:black;margin-top: 60px;"><i>Hemant Sapra....</i></h1>
</div>
</div>
			
</div>
<!--footer end here-->
</div>
</body>
</html>
"""