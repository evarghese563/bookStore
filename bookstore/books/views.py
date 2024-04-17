
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Manga
from django.shortcuts import render,redirect
import requests


def home(request):
    url = 'https://openlibrary.org/search.json?q=the+lord+of+the+rings'
    response = requests.get(url)
    data = response.json()
    print(data)
    return render(request,"books.html",{'data':data})

def base(request):
    return render(request, "base.html")


def fullmetal(request):
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



def vinlandSaga(request): 
    return render(request, "vinlandSaga.html")

def dragonball(request): 
    return render(request, "dragonball.html")

def naruto(request): 
    return render(request, "naruto.html")

def onepiece(request): 
    return render(request, "onepiece.html")

def chainsawman(request): 
    return render(request, "chainsawman.html")

def demonslayer(request): 
    return render(request, "demonslayer.html")

def myheroacademia(request): 
    return render(request, "myheroacademia.html")

def attackontitan(request): 
    return render(request, "attackontitan.html")

def tokyoghoul(request): 
    return render(request, "tokyoghoul.html")

def manga(request): 
    return render(request, "manga.html")

def squareenix(request): 
    return render(request, "squareenix.html")

def about(request): 
    return render(request, "about.html")

def contact(request): 
    return render(request, "contact.html")

def merch(request): 
    return render(request, "merch.html")






