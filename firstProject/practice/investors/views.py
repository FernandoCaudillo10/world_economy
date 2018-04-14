from django.shortcuts import render

def intro(request):
	return render(request, 'investors/intro.html')
