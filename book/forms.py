from django import forms
from .models import Book
# from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):
    # image = ImageField(label='')
    
    class Meta:
        model = Book
        fields = ('author', 'title', 'genre', 'print_length', 'ISBN', 'price', 'blurb', 'publication_date', 'photo')
    
    def clean_blurb(self):
        blurb = self.cleaned_data.get('blurb')
        if len(blurb) <= 10:
            raise forms.ValidationError("Not enough content")
            
        return blurb
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        title = title[0:50]
        return title