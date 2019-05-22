from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(blank=False, max_length=255)

class Genre(models.Model):
    genre_name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(blank=False, max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres', null=True)
    print_length = models.IntegerField(default=0)
    ISBN = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(default=0)
    blurb = models.TextField(blank=False)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', default='images/not_found.jpg')
    
    def __str__(self):
        return self.title + " ( " + self.author + " ) "