from django.urls import path 
from . import views 

app_name = 'barber'

urlpatterns = [
   path('barber/', views.barber, name='barber'),
]