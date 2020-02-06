from django.shortcuts import render
from gallery.models import Gallery


def home(request):
	gallerys = Gallery.objects
	return render(request, 'home.html', {'gallerys': gallerys})
#赋予变量，传到字典，之后去home.html写for语句

