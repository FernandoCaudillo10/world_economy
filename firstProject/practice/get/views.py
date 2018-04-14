from django.shortcuts import render

app_name = 'get'

def home(request):
	return render(request, 'get/home.html')

def about(request):
	return render(request, 'get/about.html')
