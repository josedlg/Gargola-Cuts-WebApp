from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse 
from .models import *
# Create your views here.


class Barber_View(generic.ListView):
    template_name = 'adminProf/main.html'
    context_object_name = 'ads_list'
    
    def get_queryset(self):
        return Ads.objects.all()




