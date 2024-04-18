from django.shortcuts import render
from .models import Manga
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request,"books.html")

def base(request):
    return render(request, "base.html")

def fullmetal(request):
    pushToDB(request)
    return render(request, "fullmetal.html",{})

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

def checkout(request):
    # Handle displaying DataBase data onto checkout page
    
    data = Manga.objects.all().values()
   
    site = loader.get_template('checkout.html')
    context = {'data': data,}
    return HttpResponse(site.render(context, request))

def about(request):
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

def pushToDB(request):
    if request.method =='POST':
        name = request.POST['manga']
        price = request.POST['price']
        quantity = 1
        newcart = Manga(name = name, price = price, quantity = quantity)
        newcart.save()