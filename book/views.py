from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Book

# Create your views here.
# def hello(request):
#     return HttpResponse("Hello Earth")
    
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'all_books':books})
