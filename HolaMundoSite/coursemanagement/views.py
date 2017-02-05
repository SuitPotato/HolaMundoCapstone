from django.shortcuts import render
from django.http import HttpResponse

#from .forms import CourseForm

# Create your views here.

def manage(request):
	return render(request, 'coursemanagement/manage.html')
	
def get_course(request):
	pass
