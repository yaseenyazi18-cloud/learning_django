
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="home"),
    path('collections',views.collections, name="collections"),
    path('loging',views.loging, name="loging"),
    path('register',views.register, name="register"),
    
   
]
