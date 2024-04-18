<<<<<<< HEAD

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Manga
from django.shortcuts import render,redirect
import requests
=======
from django.shortcuts import render
from .models import Manga
from django.http import HttpResponse
from django.template import loader
>>>>>>> upstream/main


def home(request):
    return render(request,"books.html")

def base(request):
    return render(request, "base.html")


def fullmetal(request):
<<<<<<< HEAD
    if request.method == 'POST':
        name = request.POST.get('manga')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')
        quantity = 1  # You can adjust this if needed

        # You may need to adjust the model field names according to your Manga model
        new_cart_item = Manga(name=name, price=price, quantity=quantity, image_url=image_url)
        new_cart_item.save()

        # Redirect to the checkout page with the newly added item
        return redirect('checkout')  # Assuming 'checkout' is the name of your checkout URL pattern

    return render(request, "fullmetal.html", {})


def add_to_cart(request, product_id):
    # Retrieve product details
    product = Manga.objects.get(pk=product_id)

    # Save product information to the cart (not shown, typically involves creating a cart model and relating it to the product)

    # Redirect to cart or checkout page
    return redirect('checkout')


def checkout(request):
    # Assuming you retrieve the parameters from the request.GET dictionary
    name = request.GET.get('name')
    price = request.GET.get('price')
    image_url = request.GET.get('image_url')

    # Pass parameters to the template
    return render(request, 'checkout.html', {'name': name, 'price': price, 'image_url': image_url})


=======
    pushToDB(request)
    return render(request, "fullmetal.html",{})
>>>>>>> upstream/main

def vinlandSaga(request):
    pushToDB(request) 
    return render(request, "vinlandSaga.html")

def dragonball(request): 
    pushToDB(request)
    return render(request, "dragonball.html")

def naruto(request): 
    pushToDB(request)
    return render(request, "naruto.html")

def onepiece(request):
    pushToDB(request) 
    return render(request, "onepiece.html")

def chainsawman(request):
    pushToDB(request) 
    return render(request, "chainsawman.html")

def demonslayer(request):
    pushToDB(request) 
    return render(request, "demonslayer.html")

def myheroacademia(request):
    pushToDB(request) 
    return render(request, "myheroacademia.html")

def attackontitan(request):
    pushToDB(request) 
    return render(request, "attackontitan.html",{})

def tokyoghoul(request):
    pushToDB(request) 
    return render(request, "tokyoghoul.html")

def manga(request):
    return render(request, "manga.html")

def squareenix(request):
    pushToDB(request) 
    return render(request, "squareenix.html")

<<<<<<< HEAD
def about(request): 
=======
def checkout(request):
    # Handle displaying DataBase data onto checkout page
    
    data = Manga.objects.all().values()
   
    site = loader.get_template('checkout.html')
    context = {'data': data,}
    return HttpResponse(site.render(context, request))

def about(request):
>>>>>>> upstream/main
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def merch(request): 
    return render(request, "merch.html")


def clearCart(request):
    # Clear the current state of the cart
    data = Manga.objects.all()
    data.delete()
    # Extract data from Data Base
    data = Manga.objects.all().values()
    site = loader.get_template('clearcart.html')
    context = {'data': data,}
    return HttpResponse(site.render(context, request))
#==========================================================================================================

<<<<<<< HEAD



=======
def pushToDB(request):
    if request.method =='POST':
        name = request.POST['manga']
        price = request.POST['price']
        quantity = 1
        newcart = Manga(name = name, price = price, quantity = quantity)
        newcart.save()
>>>>>>> upstream/main
