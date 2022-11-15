from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    # print(request.POST)
    # username = request.POST.get('username')
    # print(username)
    # password = request.POST.get('password')
    # print(password)

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None :
            print(user)
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,'wronge username or pass ')
            return redirect('account:login_user')

    return render(request,'account/index.html')


def logout_user(request):
    logout(request)
    return redirect('account:login_user')
