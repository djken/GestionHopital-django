from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

# Create your views here.
# @csrf_protect
def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') # home is a page
            else:
                messages.success(request,("There's an error! Try again!"))
                return redirect('login')
        else:
            return render(request, 'authenticate/login.html', {})
        
def logout_user(request):
    logout(request)
    messages.success(request,("You were logout!"))
    return redirect('home')

