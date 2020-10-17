#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
 <html>
<head>
<link rel="stylesheet" type="text/css" href="css/userjob.css">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
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
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu" bgcolor="red">
            <li><a href="about.py">About</a></li>
            <li><a href="login.py">Login</a></li>
            <li><a href="job.py">Job</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="contact.py">Contact</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
<!--menubar ends here-->
<div class="bb">
<div id="left1">
<center>
<h1>For Job</h1>
<hr style="border:2px solid green;width:80%;"/>
<table style="height:300px;width:40%;margin-top:50px;">
<form action="jobcode.py" method="post">
<tr>
<td><font color="black"size="4px">Title:</font></td>
<td><input type="text" name="title" required /></td>
</tr>
<tr>
<td><font color="black"size="4px">Salary:</font></td>
<td><input type="number" name="salary" required /></td>
</tr>
<tr>
<td><font color="black"size="4px">Experience:</font></td>
<td><input type="text" name="exp" required /></td>
</tr>
<tr>
<td><font color="black"size="4px">Location:</font></td>
<td><input type="text" name="location" required /></td>
</tr>
<tr>
<td><h1><input type="submit" value="send"/></h1></td>
</tr>
</form>
</table>

</div>

</div>


</div><div class="downbox">

<!--Embeded Map.....here..-->
<iframe src="https://www.google.com/maps/embed?pb=!1m17!1m11!1m3!1d3046.783988338603!2d80.8665606808103!3d26.772560872739504!2m2!1f0!2f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xae9f4362a63b5768!2sPN+INTERNATIONAL+(KARAM)%2C+Unit-I!5e1!3m2!1sen!2sin!4v1564798069948!5m2!1sen!2sin" width="100%" height="400" frameborder="0" style="border:0" allowfullscreen></iframe>
<!--Embeded Map...End..here..-->
</div>

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
<div class="col-sm-4" style="margin-top: 20px;">
<a href="www.facebook.com"><span class="fa fa-facebook fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.twitter.com"><span class="fa fa-twitter fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.instagram.com"><span class="fa fa-instagram fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.youtube.com" style="color:darkred;"><span class="fa fa-youtube fa-3x"></span></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="www.user.com"><span class="fa fa-user fa-3x"></span></a>
</div>
<div class="col-sm-4">
<h1 style="color:black;margin-top: 60px;"><i>Anil yaduvanshi....</i></h1>
</div>
</div>
	<!--footer 2nd end-->		

			
</div>
</body>
</html>
"""