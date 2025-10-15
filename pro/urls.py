from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('classes/',classes,name="classes"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('account/',account,name="account")
    # path('photo/',photo,name="photo")
]