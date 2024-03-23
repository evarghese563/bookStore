from django.contrib import admin
from django.urls import include, path
from .views import home
from .views import base
from .views import fullmetal

urlpatterns = [
    # Include the URL patterns from the 'books' app
    path("admin/", admin.site.urls),  # admin URL pattern
    path("books/", include("books.urls")),  # books URL pattern
    path("", home, name='home'),  # root URL pattern
    path("base/", base),
    path("fullmetal/", fullmetal)
]
