from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manage(request):
	return render(request, 'coursemanagement/manage.html')
