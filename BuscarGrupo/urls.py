from django.urls import path 
from BuscarGrupo import views

urlpatterns = [
    path('', views.mysite, name='mysite'), 
]