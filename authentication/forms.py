from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from book.models import Author, Genre, Book
# from pyuploadcare.dj.forms import ImageField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", help_text="No longer than 255 characters")
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    #clean_xxxx : where xxxx is the name of the field
    def clean_email(self):
        # get the username from the form
        username = self.cleaned_data.get('username')
        
        # get the email from the form as requesed_email
        requested_email = self.cleaned_data.get('email')
        
        # see if any current users is using that email
        if User.objects.filter(email=requested_email).count() > 0:
            raise forms.ValidationError("This email address is already in use.")
            
        return requested_email
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if (password1 != password2):
            raise forms.ValidationError("Password and Confirmation Password do not match.")
            
        return password2   

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']
        
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']
        
class BookForm(forms.ModelForm):
    # image = ImageField(label='')
    
    class Meta:
        model = Book
        fields = ('author', 'title', 'genre', 'print_length', 'ISBN', 'price', 'blurb', 'image')
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title=title).count() > 0:
            raise forms.ValidationError("Duplicated title")
        
        return title           