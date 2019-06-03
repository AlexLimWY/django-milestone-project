from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.author_name

class Genre(models.Model):
    genre_name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.genre_name
        
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors', null=True)
    title = models.CharField(blank=False, max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres', null=True)
    print_length = models.IntegerField(default=0)
    ISBN = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    blurb = models.TextField(blank=False)
    publication_date = models.DateTimeField(auto_now_add=True)
    photo = ImageField(blank=True)
    # image = models.ImageField(upload_to='images', default='images/not_found.jpg')
    
    def __str__(self):
        return self.title + " (" + self.author.author_name + ") "
        
    