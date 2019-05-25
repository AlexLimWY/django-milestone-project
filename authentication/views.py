from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterUserForm
from book.models import Book

# Create your views here.

def index1(request):
    books = Book.objects.all()
    return render(request, 'index1.html', {'all_books':books})

# def index(request):
#     books = Book.objects.all()
#     return render(request, 'index.html', {'all_books':books})  
    
def account_created(request):
    return render(request, 'account_created.html')
    
def logged_out(request):
    return render(request, 'logged_out.html')    
    
def invalid_login(request):
    return render(request, 'invalid_login.html')    

@login_required    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out")
    return redirect(logged_out)
    
def login(request):
    if request.method == 'POST':
        form_username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=form_username, password=password)
        if user is not None:
            auth.login(user=user, request=request)
            messages.success(request, "Welcome Back")
            return redirect(index1)
        else:
            messages.error(request, "Invalid Login")
            return redirect(invalid_login)
    else:        
        login_form = LoginForm()
        return render(request, 'login.html', {'form':login_form})
    
def register(request):
    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your account has been created!")
            return redirect(account_created)
        else:
            return render(request, 'register.html', {'form':register_form})  
    else:
        register_form = RegisterUserForm()
        return render(request, 'register.html', {'form':register_form})    
