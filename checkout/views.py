from django.shortcuts import render, HttpResponse
from django.conf import settings
from .forms import OrderForm, PaymentForm
from django.utils import timezone
from book.models import Book
from .models import Order, OrderLineItem
from django.core.mail import send_mail
from authentication.forms import RegisterUserForm
import authentication.views
import stripe
import os


# Create your views here.
def checkout(request):
    # this is to show the form
    if request.method == 'GET':
        cart = request.session.get('cart', {})
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'checkout.html', {
            'cart': cart, 
            'order_form':order_form,
            'payment_form':payment_form,
            'stripe_publishable_key':settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        # set the secret key for Stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # to process the post via POST
        cart = request.session.get('cart', {})
        total_cost = 0
        for cart_item in cart.values():
            total_cost = cart_item['quantity'] * float(cart_item['product']['price'])
           
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST) 
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_token = request.POST.get('stripe_id')
            order.purchased_at = timezone.now()
            order.ordered_by = request.user
            order.save()
            
            for cart_item in cart.values():
                book_id = cart_item['product']['id']
                book = Book.objects.get(pk=book_id)
                order_line_item = OrderLineItem(
                    book = book,
                    order = order,
                    quantity = cart_item['quantity']
                )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total_cost * 100),
                    currency = "sgd",
                    description = "Order ID #" + str(order.id),
                    source= order.stripe_token
                    )
            except stripe.error.CardError as e: 
                print (e)
                return HttpResponse("Card problem")
                
            if customer.paid:
                subject = "Your invoice for your order #" + str(order.id)
                message = "Your order has been processed and will be shipped to you shortly."
                email_from = settings.EMAIL_HOST_USER
                
                # send_to = ['mannagoodies@gmail.com']
                send_to = [request.user.email]
                send_mail(subject, message, email_from, send_to)
                return  HttpResponse("Payment Successful")
            else:
                return HttpResponse("Payment Failed")
            
        else:
            print(order_form.is_valid())
            print(payment_form.is_valid())
            print(payment_form.errors)
