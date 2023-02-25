from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email = request.POST['Email']
        password = request.POST['Password']
        c_Password = request.POST['C_Password']
        if password==c_Password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')

            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email already taken Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=First_Name,last_name=Last_Name, email=Email)

                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
