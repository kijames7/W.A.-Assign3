from django.db import models

# Create your models here.
#**************ADDED
#casing matters for how it shows up in views
class ClassSchedule(models.Model):
	email = models.EmailField()
	#validate data
	student_name = models.CharField(max_length=80,blank=True, null=True)
	professor_name = models.CharField(max_length=80,blank=True, null=True)
	course_name = models.CharField(max_length=80,blank=True, null=True)
	section_number = models.CharField(max_length=3,blank=True, null=True)
	days = models.CharField(max_length=4,blank=True, null=True)
	times = models.CharField(max_length=11,blank=True, null=True)
	location = models.CharField(max_length=10,blank=True, null=True)
	credit_hour = models.CharField(max_length=1,blank=True, null=True)
	student_id = models.CharField(max_length=80,blank=True, null=True)
	#save time when created 
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	#save time every time user updates
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	#set unicode
	def __unicode__(self): #python 3 use str instead of unicode
		return self.email



#run python manage.py makemigrations
#run python manage.py migrate