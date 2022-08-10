from django.shortcuts import render

# Create your views here.


def Trxadmin(request):

        
    return render(request,'trxadmin/index.html')

def base(request):
    return render(request,'trxadmin/base.html')


def Adminprofile(request):
    return render(request,'trxadmin/profile.html')

def share(request):
    return render(request,'trxadmin/share.html')

def member(request):
    return render(request,'trxadmin/member.html')

def coindetails(request):
    return render(request,'trxadmin/coindetails.html')

def announcement(request):
    return render(request, 'trxadmin/announcement.html')

def shareprofile(request):
    return render(request, 'trxadmin/shareprofile.html')

def memberprofile(request):
    return render(request, 'trxadmin/member profile.html')

def notifications(request):
    return render(request, 'trxadmin/notifications.html')

def singlenotification(request):
    return render(request, 'trxadmin/singlenotification.html')