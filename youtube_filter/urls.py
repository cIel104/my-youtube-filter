from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home_screen'),
    path('result/', views.result_screen, name='result_screen'),
]