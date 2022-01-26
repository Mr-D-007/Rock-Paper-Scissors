from django.contrib import admin
from django.urls import path
from rps_app import views

urlpatterns = [
    path('', views.register, name='register'),
    path('check/', views.check, name='check'),
    path('login/', views.login, name='login'),
    path('login/checklogin/', views.checklogin, name='checklogin'),
    path('checklogin/home/', views.home, name='home'),
]
