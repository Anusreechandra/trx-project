from django.urls import path
from . import views

app_name= 'home'

urlpatterns = [
    path("",views.index,name='index'),


    path("about",views.about,name='about'),
    path("contactus",views.contactus,name='contactus'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),

]