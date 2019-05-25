from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book
from authentication.views import index1
from .forms import AddToCartForm
# Create your views here.

def add_to_cart(request, id):
    book = get_object_or_404(Book, pk=id)
    cart = request.session.get('cart', {})
    
    add_to_cart_form = AddToCartForm(request.POST)
    qty = add_to_cart_form['quantity']
    
    if id not in cart:
        cart[id] = {
            'product': {
              'id': id,
              'title': book.title,
              'author_name': book.author.author_name,
              'price': book.price,
            #   'image': book.image
            },
            'quantity': int(qty.value())
        }
    else:
        cart[id]['quantity'] = cart[id]['quantity'] +  int(qty.value())
    
    request.session['cart'] = cart
    
    return redirect(view_cart)
    
def view_cart(request):
    cart = request.session.get('cart', {})
    print(cart)
    return render(request, 'view_cart.html', {
        'cart':cart
    })
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect(view_cart)
    
def remove_all_from_cart(request):
    request.session['cart'] = {}
    return redirect(index1)
