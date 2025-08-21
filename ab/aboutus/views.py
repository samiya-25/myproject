from django.shortcuts import render
from .models import Aboutus



# Create your views here.

def about(request):
    data2=Aboutus.objects.all()
    return render(request,'about.html',{'data2':data2})