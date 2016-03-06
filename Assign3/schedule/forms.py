from django import forms

from .models import ClassSchedule

#convention to name after.py file in this case form
class ClassScheduleForm(forms.ModelForm):
	class Meta:
		model = ClassSchedule
		fields = ['student_name', 'student_id', 'professor_name', 'course_name', 'section_number', 'days', 'times', 'location', 'credit_hour', 'email']
		#can use
		#exclue =['email']

	#overriding function
	def clean_email(self):
	#run through all the validators
		email = self.cleaned_data.get('email')
		email_bade, provider = email.split("@")
		domain, extension = provider.split('.')
		#if not domain == 'msudenver':
		#	raise forms.ValidationError("Please use your msudenver email.")
		if not extension == "edu":
			raise forms.ValidationError("Please use valid college email address")
		return email