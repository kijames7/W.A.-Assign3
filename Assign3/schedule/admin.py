from django.contrib import admin

# Register your models here.
#***********ADDED
#importing form models
#from someother app import 
from .forms import ClassScheduleForm
from .models import ClassSchedule

class ClassScheduleAdmin(admin.ModelAdmin):
	#display
	list_display = ["__unicode__", "student_name", "professor_name", "course_name", "section_number", "days", "times", "location", "credit_hour", "student_id", "timestamp", "updated"]
	form = ClassScheduleForm
#	class Meta:
#		model = SignUp

#                           add one more argument to the register call
admin.site.register(ClassSchedule, ClassScheduleAdmin)