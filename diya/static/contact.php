<html>
  <body>
    <?php

     $usuarioname=$_POST['S_name'];  
     $usuariomobile=$_POST['S_phone'];  
     $usuarioemail=$_POST['S_email']; 
     $usuariocourse=$_POST['course'];
     
   
     
    $recipient="yoga11.subramaniyan@gmail.com, franklin.zinavo@gmail.com";
  
    
    $subject="Free Consultation Form";
    
    
     $mailheader="";
      $mailheader .="form:".$usuarioname."\r\n";
      $mailheader .="Mobile Number:".$usuariomobile."\r\n";
      $mailheader .="E-mail ID:".$usuarioemail."\r\n";
      $mailheader .="Message:".$usuariocourse."\r\n";
  
  mail($recipient,$subject,$mailheader) or die("Error!");
  
    echo"Successfully submited";
?>  
<style>
body{
	background-color:#683853;
	height:100%;
	}
.thks{
	text-align:center;
	padding:150px;
	color:#fff;
	font-size:50px;
	}
a{
text-decoration:none;
color:#CE0614;
font-size:20px;
}
a:hover{
	text-decoration:underline;
	color:#17AEE7;
}
</style>
</head>
<body>
<div class="thks">
<p>Thanks for being awesome! We have received your message we would contact you later</p>
<div>Back To <a href="diya.html">  Home Page</a></div>
</div>
  </body>  
</html>


