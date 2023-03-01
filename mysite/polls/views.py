from unittest import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Member

# Create your views here.
def home(request):
    return render(request,'polls/post/home.html')

def login(request):
     if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Member.objects.filter(email=email,password=password).exists():
            return redirect('/')
        else:
            return HttpResponse('Xatolik bor email yoki passwordda')
     else:
        return render(request,'polls/registration/login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=Member(username=username,email=email,password=password)
        user.save()
        return redirect('/')
    else:
        return render(request,'polls/registration/register.html')