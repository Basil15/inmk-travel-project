from django.shortcuts import render
from .models import place,team

# Create your views here.
def index(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'result':obj,'team':obj2})
