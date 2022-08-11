from multiprocessing import context
from django import views
from django.shortcuts import render

# Create your views here.


def index(request):
    context ={
        'is_index':True
    }
    return render(request, 'member/index.html', context)
    

def profile(request):
    return render(request, 'member/profile.html')

def transactions(request):
    context ={
        'is_transactions':True
    }
    return render(request, 'member/transactions.html',context)

def rewards(request):
    context ={
        'is_rewards':True
    }
    return render(request, 'member/rewards.html',context)

def kyc_home(request):
    return render(request, 'member/kyc-home.html')

def coin_details(request):
    context ={
        'is_coin_details':True
    }
    return render(request, 'member/coin-details.html',context)

def kyc(request):
    return render(request, 'member/kyc.html')