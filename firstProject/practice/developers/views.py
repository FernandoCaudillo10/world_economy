from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def intro(request):
	return render(request, 'developers/intro.html')	

def simple_upload(request):
	
	if request.method == 'POST' and request.FILES['myfile']:
		print("hello")
		myfile = request.FILES['myfile']
		print(myfile)
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'developers/fileupload.html', {
			'uploaded_file_url': uploaded_file_url
		})
	return render(request, 'developers/fileupload.html')
