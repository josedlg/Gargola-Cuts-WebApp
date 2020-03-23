from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
# Create your views here.



def barber(request):
    return render(request,'adminProf/main.html')