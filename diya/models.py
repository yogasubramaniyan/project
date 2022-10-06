from django.db import models

# Create your models here.
class aboutus(models.Model):

	logo_img = models.ImageField(upload_to="thumnail/")

	nav_link = models.CharField(max_length=100, blank=True,null=True)
	nav_link1 = models.CharField(max_length=100, blank=True,null=True)
	nav_link2 = models.CharField(max_length=100, blank=True,null=True)
	nav_link3 = models.CharField(max_length=100, blank=True,null=True)
	nav_link4 = models.CharField(max_length=100, blank=True,null=True)
	nav_link5 = models.CharField(max_length=100, blank=True,null=True)
	nav_link6 = models.CharField(max_length=100, blank=True,null=True)
	nav_link7 = models.CharField(max_length=100, blank=True,null=True)


	banner_img = models.ImageField(upload_to="thumnail/")
	banner_img1 = models.ImageField(upload_to="thumnail/")

	title = models.CharField(max_length=100, blank=True,null=True)
	head = models.CharField(max_length=100, blank=True,null=True)
	content = models.TextField(max_length=5000, blank=True,null=True)
	content1 = models.TextField(max_length=5000, blank=True,null=True)
	content2 = models.TextField(max_length=5000, blank=True,null=True)
	thumnail = models.ImageField(upload_to="thumnail/")
	thumnail1 = models.ImageField(upload_to="thumnail/")
	thumnail2 = models.ImageField(upload_to="thumnail/")
	para = models.CharField(max_length=100, blank=True,null=True)
	para1 = models.CharField(max_length=100, blank=True,null=True)
	para2 = models.CharField(max_length=100, blank=True,null=True)
	slug = models.SlugField(max_length=100)
	
	course_head = models.TextField(max_length=5000, blank=True,null=True)
	course_para = models.TextField(max_length=5000, blank=True,null=True)
	
	course_list= models.ImageField(upload_to="thumnail/")
	course_list1= models.ImageField(upload_to="thumnail/")
	course_list2= models.ImageField(upload_to="thumnail/")
	
	App_title = models.CharField(max_length=100, blank=True,null=True)
	App_head = models.CharField(max_length=100, blank=True,null=True)
	
	
	Acc_head = models.CharField(max_length=100, blank=True,null=True)
	Acc_image = models.ImageField(upload_to="thumnail/")
	Acc_image1= models.ImageField(upload_to="thumnail/")
	Acc_image2= models.ImageField(upload_to="thumnail/")
	Acc_image3= models.ImageField(upload_to="thumnail/")
	Acc_image4= models.ImageField(upload_to="thumnail/")
	
	Frequently_head = models.CharField(max_length=100, blank=True,null=True)
	
	choice_para = models.TextField(max_length=5000, blank=True,null=True)
	choice_para1 = models.TextField(max_length=5000, blank=True,null=True)
	choice_para2 = models.TextField(max_length=5000, blank=True,null=True)
	choice_para3 = models.TextField(max_length=5000, blank=True,null=True)
	
	best_para = models.TextField(max_length=5000, blank=True,null=True)
	best_para1 = models.TextField(max_length=5000, blank=True,null=True)
	best_para2 = models.TextField(max_length=5000, blank=True,null=True)
	best_para3 = models.TextField(max_length=5000, blank=True,null=True)
	best_para4= models.TextField(max_length=5000, blank=True,null=True)
	best_para5 = models.TextField(max_length=5000, blank=True,null=True)
	best_para6 = models.TextField(max_length=5000, blank=True,null=True)
	best_para7 = models.TextField(max_length=5000, blank=True,null=True)
	best_para8= models.TextField(max_length=5000, blank=True,null=True)
	best_para9 = models.TextField(max_length=5000, blank=True,null=True)
	best_para10 = models.TextField(max_length=5000, blank=True,null=True)
	best_para11= models.TextField(max_length=5000, blank=True,null=True)
	best_para12= models.TextField(max_length=5000, blank=True,null=True)
	best_para13= models.TextField(max_length=5000, blank=True,null=True)
	best_para14= models.TextField(max_length=5000, blank=True,null=True)
	best_para15= models.TextField(max_length=5000, blank=True,null=True)
	best_para16= models.TextField(max_length=5000, blank=True,null=True)
	best_para17= models.TextField(max_length=5000, blank=True,null=True)
	
	INC_para = models.TextField(max_length=5000, blank=True,null=True)
	INC_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	KNC_para = models.TextField(max_length=5000, blank=True,null=True)
	KNC_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	RGUHS_para = models.TextField(max_length=5000, blank=True,null=True)
	RGUHS_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	Found_para = models.TextField(max_length=5000, blank=True,null=True)
	Found_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	salery_para = models.TextField(max_length=5000, blank=True,null=True)
	salery_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	saleryGov_para = models.TextField(max_length=5000, blank=True,null=True)
	saleryGov_para1 = models.TextField(max_length=5000, blank=True,null=True)
	
	rank_para = models.TextField(max_length=5000, blank=True,null=True)
	rank_para1 = models.TextField(max_length=5000, blank=True,null=True)
	rank_para2 = models.TextField(max_length=5000, blank=True,null=True)
	rank_para3 = models.TextField(max_length=5000, blank=True,null=True)
	rank_para4 = models.TextField(max_length=5000, blank=True,null=True)
	rank_para5 = models.TextField(max_length=5000, blank=True,null=True)
	
	Uk_para = models.TextField(max_length=5000, blank=True,null=True)
	Uk_para1 = models.TextField(max_length=5000, blank=True,null=True)
	Uk_para2 = models.TextField(max_length=5000, blank=True,null=True)
	Uk_para3 = models.TextField(max_length=5000, blank=True,null=True)
	Uk_para4 = models.TextField(max_length=5000, blank=True,null=True)
	Uk_para5 = models.TextField(max_length=5000, blank=True,null=True)
	
	college_para = models.TextField(max_length=5000, blank=True,null=True)
	college_para1 = models.TextField(max_length=5000, blank=True,null=True)
	college_para2 = models.TextField(max_length=5000, blank=True,null=True)
	college_para3 = models.TextField(max_length=5000, blank=True,null=True)
	college_para4 = models.TextField(max_length=5000, blank=True,null=True)
	college_para5 = models.TextField(max_length=5000, blank=True,null=True)
	college_para6= models.TextField(max_length=5000, blank=True,null=True)
	college_para7 = models.TextField(max_length=5000, blank=True,null=True)
	college_para8 = models.TextField(max_length=5000, blank=True,null=True)
	college_para9 = models.TextField(max_length=5000, blank=True,null=True)
	college_para10 = models.TextField(max_length=5000, blank=True,null=True)
	college_para11= models.TextField(max_length=5000, blank=True,null=True)
	college_para12 = models.TextField(max_length=5000, blank=True,null=True)
	college_para13 = models.TextField(max_length=5000, blank=True,null=True)
	college_para14 = models.TextField(max_length=5000, blank=True,null=True)
	
	colleges_para = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para1 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para2 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para3 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para4 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para5 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para6= models.TextField(max_length=5000, blank=True,null=True)
	colleges_para7 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para8 = models.TextField(max_length=5000, blank=True,null=True)
	colleges_para9 = models.TextField(max_length=5000, blank=True,null=True)
	
	Gui_title = models.CharField(max_length=100, blank=True,null=True)
	Gui_head = models.CharField(max_length=100, blank=True,null=True)
	
	con_head = models.CharField(max_length=100, blank=True,null=True)
	con_para1 = models.TextField(max_length=5000, blank=True,null=True)
	con_para2 = models.TextField(max_length=5000, blank=True,null=True)
	con_para3 = models.TextField(max_length=5000, blank=True,null=True)
	con_para4 = models.TextField(max_length=5000, blank=True,null=True)
	con_image= models.ImageField(upload_to="thumnail/")
	con_image1 = models.ImageField(upload_to="thumnail/")
	con_image2 = models.ImageField(upload_to="thumnail/")
	
	foot_logo= models.ImageField(upload_to="thumnail/")
	foot_cont = models.TextField(max_length=5000, blank=True,null=True)
	
	qui_link = models.CharField(max_length=100, blank=True,null=True)
	qui_link1 = models.CharField(max_length=100, blank=True,null=True)
	qui_link2 = models.CharField(max_length=100, blank=True,null=True)
	qui_link3= models.CharField(max_length=100, blank=True,null=True)
	qui_link4= models.CharField(max_length=100, blank=True,null=True)
	qui_link5= models.CharField(max_length=100, blank=True,null=True)
	qui_link6= models.CharField(max_length=100, blank=True,null=True)
	qui_link7= models.CharField(max_length=100, blank=True,null=True)
	qui_links= models.ImageField(upload_to="thumnail/")
	
	cou_link = models.CharField(max_length=100, blank=True,null=True)
	cou_link1 = models.CharField(max_length=100, blank=True,null=True)
	cou_link2 = models.CharField(max_length=100, blank=True,null=True)
	cou_link3= models.CharField(max_length=100, blank=True,null=True)
	cou_link4= models.CharField(max_length=100, blank=True,null=True)
	cou_link5= models.CharField(max_length=100, blank=True,null=True)
	
	
	copy = models.CharField(max_length=100, blank=True,null=True)
	ffoot_imag = models.ImageField(upload_to="thumnail/")
	ffoot_imag1 = models.ImageField(upload_to="thumnail/")
	ffoot_imag2 = models.ImageField(upload_to="thumnail/")
	ffoot_imag3 = models.ImageField(upload_to="thumnail/")
	ffoot_imag4 = models.ImageField(upload_to="thumnail/")
	
	