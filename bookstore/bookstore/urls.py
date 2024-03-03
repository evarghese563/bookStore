from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #the bottom line points to the polls.urls file    
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
]