from django import forms
from .models import Book

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('author', 'title', 'genre', 'print_length', 'ISBN', 'price', 'blurb', 'publication_date', 'image')
    
    def clean_blurb(self):
        blurb = self.cleaned_data.get('blurb')
        if len(blurb) <= 10:
            raise forms.ValidationError("Not enough content")
            
        return blurb
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        title = title[0:50]
        return title