#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "show all complain"
import MySQLdb
print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/userjob.css"/>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>

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
<img src="images/32.jpeg" id="image2"/>
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
      
	  <a class="navbar-brand" href="index.html">Home</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="about.py">About us</a></li>
        <li><a href="login.py">Login</a></li>
		<li><a href="product.py">Products</a></li>
		<li><a href="job.py">Jobs</a></li>
        <li><a href="contact.py">Contact us</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <form class="navbar-form navbar-left" role="search">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
       
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
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
	
	
<!--start 1st footer-->
<footer id="footer">
 <div class="footer-top">
  <div class="container">
   <div class="row">
    <div class="col-lg-4 col-md-6 footer-info">
	<h4>WebsiteName</h4><br/>
	<p>KARAM embarks on its journey to become a <br/><br/>
	multinational company and launches <br/>
	its own company in Europe by the name of KRATOS<br/>
	Safety based in Lyon France to cater to the entire European market. <br/><br/><br/>
	<a href="www.karam.com">www.karam.com</a>
	</p>
	</div>
	<div class="col-lg-2 col-md-6 footer-links">
	 <h4>Useful Links</h4>
	 <ul>
	 <li><a href="#">GOOGLE+</a></li>
	 <li><a href="#">JOB</a></li>
	 <li><a href="#">HISTORY</a></li>
	 <li><a href="#">EMPLOYEE</a></li>

	 </ul>
	 </div>
	 <div class="col-lg-3 col-md-6 footer-contant">
	 <h4>Contact Us</h4>
	 <p>
	 24 Block D <br>
	 Mayur Vihar, New Delhi<br>
	 India<br>
      <strong>Phone:</strong>+9120313518<br>
      <strong>Email:</strong>website@gmail.com<br>
      </p>
      <div class="social links">
        <a href="#" class="twitter"><i class="fa fa-twitter"></i></a>
        <a href="#" class="twitter"><i class="fa fa-facebook"></i></a>
        <a href="#" class="twitter"><i class="fa fa-instagram"></i></a>
        <a href="#" class="twitter"><i class="fa fa-google-plus"></i></a>
        <a href="#" class="twitter"><i class="fa fa-linkedin"></i></a>	
       </div>
      </div>
	    <div class="col-lg-3 col-md-6 footer-newsletter">
		  <h4>Our newsletter</h4>
		  <p>KARAM is India leading Personal Protective Equipment Manufacturing enterprise and is rated as one of the 
		  finest Indian companies providing world class PPE.KARAM ranks as the number one Company in the field of Personal Safety in the country.
	      </p>
		  <form accept="" method="post">
		  <input type="email" name="email"><input type="submit" value="subscribe">
		  </form>
		</div>
     </div>
	 </div>
	</div>
	
	</footer>
	<!--footer 1st end-->
	
<!--footer 2nd start-->
<div class="d-flex" style="min-height:100px;background-color:rgba(63,79,89,0.7);color:black;width:100%;">
<div class="col-sm-4">
<h3>Copyright &copy; SOFTPRO..</h3>

</div>

<div class="col-sm-4">
<h2 style="color:black;margin-top: 20px;position:relative;"><i></i></h2>
</div>

<div class="col-sm-4">
<h2 style="color:black;margin-top: 50px;position:relative;float:right;"><i>Anil yaduvanshi....</i></h2>
</div>

</div>
	<!--footer 2nd end-->
</div>
</body>
</html>
"""