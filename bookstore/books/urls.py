from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("busy/", views.base, name="base"),
    path("fullmetal/", views.fullmetal, name='fullmetal'),
    path("vinlandSaga/", views.vinlandSaga, name='vinlandSaga'),
    path("dragonball/", views.dragonball, name='dragonball'),
    path("naruto/", views.naruto, name='naruto'),
    path("onepiece/", views.onepiece, name='onepiece'),
    path("chainsawman/", views.chainsawman, name='chainsawman'),
    path("demonslayer/", views.demonslayer, name='demonslayer'),
    path("myheroacademia/", views.myheroacademia, name='myheroacademia'),
    path("attackontitan/", views.attackontitan, name='attackontitan'),
    path("tokyoghoul/", views.tokyoghoul, name='tokyoghoul'),
    path("manga/", views.manga, name='manga'),
    path("squareenix/", views.squareenix, name='squareenix'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("checkout/", views.checkout, name='checkout'),
    path("merch/", views.merch, name='merch'),
    path("books/fullmetal/checkout/", views.checkout, name='checkout')

]