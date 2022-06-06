from django.shortcuts import render, redirect
#from .form import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.form import *

def index(request):
    return render(request, 'index.html', {})


def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')
    return render(request, 'login.html', {})


def home(request):
    return render(request, 'home.html', {})


def logoutUser(request):
    logout(request)
    return redirect(request, 'accounts/index.html', {})


# Create your views here.
def man_list(args):
    pass


def manager(request):
    form = ManagerForm()
    tech_list = Manager1.objects.all()
    if request.method == 'POST':
        form = Manager1(request.POST)
        post = form.save(commit=False)
        post.save()
    return render(request, 'Manager.html', {'form': form, 'man_list': man_list})


def emp_list(args):
    pass


def employee(request):
    form = EmployeeForm()
    stud_list = Employee1.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        post = form.save(commit=False)
        post.save()
    return render(request, 'Employee.html', {'form': form, 'emp_list': emp_list})

def teja(request):
    form = TejaForm()
    stud_list = Teja.objects.all()
    if request.method == 'POST':
        form = TejaForm(request.POST)
        post = form.save(commit=False)
        post.save()
    return render(request, 'Employee.html', {'form': form, 'emp_list': emp_list})