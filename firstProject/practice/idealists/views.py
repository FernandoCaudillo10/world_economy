from django.shortcuts import render

def intro(request):
	return render(request, 'idealists/intro.html')
