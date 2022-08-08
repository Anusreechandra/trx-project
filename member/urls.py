from django.urls import path
from . import views

app_name= 'member'

urlpatterns = [
   
   path("", views.index, name='index'),
   path('profile/', views.profile, name='profile'),
   path('transactions/', views.transactions, name='transactions'),
   path('rewards/', views.rewards, name='rewards')

]