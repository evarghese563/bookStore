from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("busy/", views.base, name="base"),
    path("fullmetal/", views.fullmetal, name='fullmetal')
]