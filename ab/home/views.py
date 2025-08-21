from django.shortcuts import render
from.models import Home


def home(request):
    data=Home.objects.all()
    print("data")
    return render(request,'index.html',{'data':data})
# Create your views here.


