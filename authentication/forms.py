from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
            raise forms.ValidationError("This email is already in use.")
            
        return requested_email
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if (password1 != password2):
            raise forms.ValidationError("Password and Confirmation Password do not match.")
            
        return password2    