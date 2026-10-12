from django.urls import path
from .views import * 


urlpatterns = [
    path('', get_all, name='show'),
    path('fidbek/', fidbek, name='fidbek'),
]
