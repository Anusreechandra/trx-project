from django.urls import path
from . import views

app_name= 'trxadmin'

urlpatterns = [
    path("",views.Trxadmin,name='Trxadmin'),
    path("",views.base,name='base'),
    path("Adminprofile",views.Adminprofile,name='Adminprofile'),


    

]
