from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Manga
import requests


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

    return render(request, "checkout.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def merch(request): 
    return render(request, "merch.html")



def pushToDB(request):
    if request.method =='POST':
        name = request.POST['manga']
        price = request.POST['price']
    
        quantity = 1

        newcart = Manga(name = name, price = price, quantity = quantity)
        newcart.save()