from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('Login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('contactus',views.contactus,name="contactus"),

]
