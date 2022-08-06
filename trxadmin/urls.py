from django.urls import path
from . import views

app_name= 'trxadmin'

urlpatterns = [
    path("",views.Trxadmin,name='Trxadmin'),
    path("",views.base,name='base'),
    path("Adminprofile",views.Adminprofile,name='Adminprofile'),
    path("share",views.share,name='share'),
    path("member",views.member,name='member'),
    path("coindetails",views.coindetails,name='coindetails'),


    

]
