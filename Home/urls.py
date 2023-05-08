from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),    
    path("register", views.register, name='register'),
    path("about", views.about, name='about'),
    path("singing", views.singing, name='singing'),
    path("guitar", views.guitar, name='guitar'),
    path("other_instruments", views.other_instruments, name='other_instruments'),
    path("contact", views.contact, name='contact'),
    path("card1", views.card1, name='card1'),
    path("card2", views.card2, name='card2'),
    path("card3", views.card3, name='card3'),
    path("card4", views.card4, name='card4'),
    path("search", views.search, name='search'),
]