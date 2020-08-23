from django.shortcuts import render
from .models import projecto

# Create your views here.
def portafolio(request):
	projectos = projecto.objects.all()
	return render(request,'portafolio/portafolio.html',{'projectos':projectos}) 