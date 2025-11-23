from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('booking/', views.booking),
    path('doctor/', views.doctor),
    path('contact/', views.contact),
    path('department/', views.department),
       
]


