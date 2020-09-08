from django.urls import path
from . import views

urlpatterns = [
    path('udMain/', views.udMain, name='udMain'),
    path('name/', views.name, name='name'),
    path('game/', views.udGame, name='game'),
]
