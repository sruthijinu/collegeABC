from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request,"Password is not match with your username")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        password1 = request.POST['psw-repeat']
        if password==password1:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"Sorry....Username already exist")
                 return redirect('register')

             else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')


def formfill(request):
    if request.method == 'POST':

         messages.info(request, "Order confirmed")
    return render(request,'formfill.html')



def detail1(request):

    return render(request,'detail1.html')

def detail2(request):

    return render(request,'detail2.html')
def detail3(request):

    return render(request,'detail3.html')

def detail4(request):

    return render(request,'detail4.html')

def detail5(request):

    return render(request,'detail5.html')