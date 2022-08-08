from django import views
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'member/index.html')


def profile(request):
    return render(request, 'member/profile.html')

def transactions(request):
    return render(request, 'member/transactions.html')

def rewards(request):
    return render(request, 'member/rewards.html')