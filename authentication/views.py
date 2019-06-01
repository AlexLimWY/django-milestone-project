from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterUserForm, BookForm, AuthorForm, GenreForm
from book.models import Book, Author, Genre
from shopping_cart.forms import AddToCartForm

# Create your views here.

def index1(request):
    addtocart_form = AddToCartForm()
    if 'search_terms' in request.GET:
        search_terms = request.GET.get('search_terms')
        books = Book.objects.filter(title__icontains=search_terms)
    else:
        books = Book.objects.all()    
    return render(request, 'index1.html', {'all_books':books, 'form':addtocart_form})

def manage_authors(request):
    authors = Author.objects.all()
    return render(request, 'manage_authors.html', {'all_authors': authors})
    
def manage_genres(request):
    genres = Genre.objects.all()
    return render(request, 'manage_genres.html', {'all_genres': genres})    
    
def edit(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        submitted_form = BookForm(request.POST, instance=book)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(index1)
    else:    
    
        edit_form = BookForm(instance=book)
        return render(request, 'edit.html', {
            'form':edit_form
    }) 

def edit_genre(request, id):
    genre = get_object_or_404(Genre, pk=id)
    if request.method == "POST":
        submitted_form = GenreForm(request.POST, instance=genre)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(manage_genres)
    else:    
    
        editgenre_form = GenreForm(instance=genre)
        return render(request, 'edit_genre.html', {
            'form':editgenre_form
    }) 
    
def delete_genre(request, id):
    genre = get_object_or_404(Genre, pk=id)
    if request.method == "POST":
        genre.delete()
        return redirect(manage_genres)
    else:
        return render(request, 'confirm_delete_genre.html', {
            'each_genre':genre
        })      

def edit_author(request, id):
    author = get_object_or_404(Author, pk=id)
    if request.method == "POST":
        submitted_form = AuthorForm(request.POST, instance=author)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(manage_authors)
    else:    
    
        editauthor_form = AuthorForm(instance=author)
        return render(request, 'edit_author.html', {
            'form':editauthor_form
    }) 

def delete_author(request, id):
    author = get_object_or_404(Author, pk=id)
    if request.method == "POST":
        author.delete()
        return redirect(manage_authors)
    else:
        return render(request, 'confirm_delete_author.html', {
            'each_author':author
        })    

def delete(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        book.delete()
        return redirect(index1)
    else:
        return render(request, 'confirm_delete.html', {
            'each_book':book
        })
        
def add(request):
    if request.method == "POST":
        submitted_form = BookForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(index1)
        else:
            return render(request, "add.html", {
                'form':submitted_form
            })
        
    else:
        addbook_form = BookForm()
        return render(request, "add.html", {
            'form' : addbook_form
        })

def add_genre(request):
    if request.method == "POST":
        submitted_form = GenreForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(manage_genres)
        else:
            return render(request, "add_genre.html", {
                'form':submitted_form
            })
        
    else:
        addgenre_form = GenreForm()
        return render(request, "add_genre.html", {
            'form' : addgenre_form
        })

def add_author(request):
    if request.method == "POST":
        submitted_form = AuthorForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(manage_authors)
        else:
            return render(request, "add_author.html", {
                'form':submitted_form
            })
        
    else:
        addauthor_form = AuthorForm()
        return render(request, "add_author.html", {
            'form' : addauthor_form
        })
    
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
