from django.test import TestCase
from .models import Author, Genre, Book
from decimal import *

# Create your tests here.
class AuthorTest(TestCase):
    
    def test_CreateAuthor(self):
        a= Author(author_name="David")
        a.save()
        
        b= Author.objects.all().get(pk=a.id)
        self.assertEqual(a.author_name, b.author_name)
        self.assertEqual(a.id, b.id)        
        
class GenreTest(TestCase):
    
    def test_CreateGenre(self):
        a = Genre(genre_name="Thriller")
        a.save()
        
        # Test if we can retrieve the genre from the database
        b = Genre.objects.all().get(pk=a.id)
        self.assertEqual(a.genre_name, b.genre_name)
        self.assertEqual(a.id, b.id)
        
class BookTest(TestCase):
    def test_CreateBook(self):
        a= Author(author_name="David")
        a.save()        

        g = Genre(genre_name="Thriller")
        g.save()
        
        b= Book(author=a, title='Redemption', genre=g, print_length=433, ISBN='1538761416', price=10.58, blurb='test content')
        b.save()
        
        c = Book.objects.all().get(pk=b.id)
        self.assertEqual(b.author, c.author)
        self.assertEqual(b.title, c.title)
        self.assertEqual(b.genre, c.genre)
        self.assertEqual(b.print_length, c.print_length)
        self.assertEqual(b.ISBN, c.ISBN)
        self.assertAlmostEqual(Decimal(b.price), Decimal(c.price))
        self.assertEqual(b.blurb, c.blurb)
        self.assertEqual(b.id, c.id)