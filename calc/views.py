#from pyexpat.errors import messages
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='')
def base(request):
    return render(request,'base.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('check/')
            
        else:
            messages.info(request,"Username OR Password INVALID")
            return redirect('/')
    else:
        return render(request,'login.html',{'name':'raju'})    



