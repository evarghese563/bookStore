from django.contrib import admin
from django.urls import include, path
from .views import home
from .views import base
from .views import fullmetal
from .views import vinlandSaga
from .views import dragonball
from .views import naruto
from .views import onepiece
from .views import chainsawman
from .views import demonslayer
from .views import myheroacademia
from .views import attackontitan
from .views import tokyoghoul
from .views import manga
from .views import merch


urlpatterns = [
    # Include the URL patterns from the 'books' app
    path("admin/", admin.site.urls),  # admin URL pattern
    path("books/", include("books.urls")),  # books URL pattern
    path("", home, name='home'),  # root URL pattern
    path("base/", base),
    path("fullmetal/", fullmetal),
    path("vinlandSaga/", vinlandSaga),
    path("dragonball/", dragonball),
    path("naruto/", naruto),
    path("onepiece/", onepiece),
    path("chainsawman/", chainsawman),
    path("demonslayer/", demonslayer),
    path("myheroacademia/", myheroacademia),
    path("attackontitan/", attackontitan),
    path("tokyoghoul/", tokyoghoul),
    path("manga/", manga),
    path("merch/", merch)
]
