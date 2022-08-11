from django.shortcuts import render
 

# Create your views here.


def index(request):

        context={
            "is_index":True,

        }
        return render(request,'home/index.html',context)  



def about(request):

     context={
            "is_about":True,

        }
        
     return render(request,'home/about.html',context)

def contactus(request):
     context={
            "is_contactus":True,

        }
  
     return render(request,'home/contactus.html',context)
        
def login(request):
   
  
     return render(request,'home/login.html')

def signup(request):
  
    return render(request,'home/signup.html')

def faq(request):
    context={
            "is_faq":True,

        }
  
    return render(request,'home/faq.html',context)



