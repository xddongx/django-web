from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def UserCreateForm(POST):
    pass


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            user = User.objects.create_user(username=username,password=password)
            user_check = auth.authenticate(request, username=username, password=password)
            if user_check is not None:
                auth.login(request,user_check)
                return redirect('/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')