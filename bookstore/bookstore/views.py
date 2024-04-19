from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
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
    return render(request, "fullmetal.html")

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

def merch(request):
    return render(request, "merch.html")