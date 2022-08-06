from django.shortcuts import render

# Create your views here.


def Trxadmin(request):

        
    return render(request,'trxadmin/index.html')

def base(request):
    return render(request, 'trxadmin/base.html')


def Adminprofile(request):
    return render(request, 'trxadmin/profile.html')