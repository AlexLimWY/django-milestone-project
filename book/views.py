from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from authentication.forms import LoginForm, RegisterUserForm
from .models import Book

# Create your views here.
# def hello(request):
#     return HttpResponse("Hello Earth")
    
def index(request):
    if 'search_terms' in request.GET:
        search_terms = request.GET.get('search_terms')
        books = Book.objects.filter(title__icontains=search_terms)
    else:
        books = Book.objects.all()
    return render(request, 'index.html', {'all_books':books})
