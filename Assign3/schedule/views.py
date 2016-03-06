from django.shortcuts import render

from .forms import ClassScheduleForm

# Create your views here.
def home(request):
	#context
	title = 'Welcome to the class scheduler'
	#if request.user.is_authenticated():
		#title = "My Title %s" %(request.user)
	#add a form


#	if request.method == "POST":
#		print request.POST
	form = ClassScheduleForm(request.POST)
	context = {
		"title": title,
		"form":form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#print instance.email
		#print instance.timestamp
		context = {
			"title": "Class has now been scheduled"
		}


	return render(request, "home.html", context)