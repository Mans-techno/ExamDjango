from django.urls import path
from .views import * 


urlpatterns = [
    path('', get_all, name='show'),
    path('fidbek/', fidbek, name='fidbek'),
    path('kino/', kino_list, name='kino_list'),
    path('kino/create/', create_kino, name='kino_create'),
    path('kino/<int:pk>/update/', update_kino, name='kino_update'),
    path('kino/<int:pk>/delete/', delete_kino, name='kino_delete'),
]
