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

