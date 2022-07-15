from django.contrib import admin
from django.urls import path
from first import views

urlpatterns = [
    path('', views.index , name="first"),  # Calls the index function from views
    path('about', views.about , name="about"),# Calls the about function from views
    path('services', views.services , name="services"),# Calls the services function from views
    path('contact', views.contact , name="contact"),# Calls the contact function from views
] 