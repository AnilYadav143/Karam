#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
 <html>
<head>

<style>
#slider
{
height:400px;
width:100%;
background-size:cover;
//border:1px solid;
//margin: 50px auto;
}

</style>
<script>
var img=["hemant.jpg","rajesh.jpg","rohit.jpg","o6.jpg"];
var i=0;
function slide()
{
var div=document.getElementById("slider");
div.style.backgroundImage="url('images/"+img[i]+"')";
i++;
if(img.length==i)
{
i=0;
}
window.setTimeout("slide()",3000);

}
</script>
<script>
var img=["hemant.jpg","rajesh.jpg","rohit.jpg","o6.jpg"];
var i=0;
function slide1()
{
var div=document.getElementById("slider1");
div.style.backgroundImage="url('images/"+img[i]+"')";
i++;
if(img.length==i)
{
i=0;
}
window.setTimeout("slide1()",3000);
}
</script>

<link rel="stylesheet" type="text/css" href="css/about.css">
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
<script src="js/jquery-2.1.0.min.js">
</script>
<script src="js/bootstrap.min.js">
</script>
</head>
<body onload="slide()">

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



<div class="box1">
<div class="box2">
<div id="slider">

</div>
</div>
<div class="box3">

<div class="abouthr">

<h2>Mr. Hemant Sapra <br/>
(President Global Marketing)</h2>
<div class="hemantrp">
<img src="images/hemant.jpg" id="profile"/>
</div>

 <h4><font size="8px">W</font>ith deep understanding of Customer needs<br/>
and a dedicated approach towards excellence<br/>
 Mr Hemant Sapra of personal and <br/><br/>
 marketing skills have enabled to build trust and<br/> <br/>
 everlasting bonds not only with Customers<br/><br/>
 across the globe but also with his team members Mr<br/>
Sapra is also the President of Safety Appliances Manufacturing Association in India.
</h4>
</div>

<div class="abouthr" style="background-color:grey;">

<h1>Mr. Rajesh Nigam <br/>
(President, 
 Technical)</h1>
<div class="hemantrp">
<img src="images/rajesh.jpg" id="profile" style="margin-top:22px;"/>
</div>

 <h4><font size="7px">m</font>r Rajesh Nigam hails from one of the most premium Engineering<br/>
 Institutes of the country IIT-Kanpur, as a B.Tech in Metallurgical Engineering. <br/>
His technical expertise and unique ability to apply his engineering <br/>
skills has spearheaded the success behind launch of a wide range of highly <br/>
technical safety products in the Indian as well as the overseas market.</h4>
</div>


</div>
<div class="box4">
<div id="slider1">

</div>
</div>



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

<div class="col-sm-4">
<h2 style="color:black;margin-top: 20px;position:relative;"><i></i></h2>
</div>

<div class="col-sm-4">
<h2 style="color:black;margin-top: 50px;position:relative;float:right;"><i>Anil yaduvanshi....</i></h2>
</div>

</div>
	<!--footer 2nd end-->

		<!-- 2nd Footer End-->	
</div>
</body>
</html>
"""