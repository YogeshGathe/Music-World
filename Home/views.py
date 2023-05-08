import email
from genericpath import exists
import http
from multiprocessing import context
import re
from django.shortcuts import render, HttpResponse, redirect
from Home.models import Contact
from datetime import date, datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages
from api.models import Chord
from django.db.models import Q
from autoscraper import AutoScraper
import requests



# Create your views here.
def index(request):
    context= {
        'variable' : "This is it"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage!")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            messages.success(request, '{} successfuly logged in!'.format(username))
            return redirect("/")
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists(): 
                messages.error(request, 'Username taken! Try a different one.')
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Duplicate email found! Try a different one.')
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save();
                messages.success(request, 'User Created Successfuly!')
                return redirect("login")

                
        else:
            messages.error(request, 'Password not matching!')
        return render(request, "register.html")

    else:
        return render(request, "register.html")

def about(request):
    return render(request, 'about.html')

def guitar(request):
    return render(request, 'guitar.html')   
    
def singing(request):
    return render(request, 'singing.html')

def other_instruments(request):
    return render(request, 'other_instruments.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact= Contact(name=name, phone=phone, email=email, message=message, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')

def card1(request):
    return render(request, 'card1.html') 

def card2(request):
    return render(request, 'card2.html') 

def card3(request):
    return render(request, 'card3.html') 

def card4(request):
    return render(request, 'card4.html') 

# def search(request):
#     data=Chord.objects.all()
#     if 'search' in request.GET:
#         search=request.GET['search']
#         data=Chord.objects.filter(Q(title__icontains=search)|Q(singer__icontains=search))
#     return render(request, 'search.html', {'data':data}) 

def search(request):
    url='https://www.google.com/search?q=guitar+chords+of+song+jeena+jeena'
    expected_output =['https://tabs.ultimate-guitar.com/tab/misc-soundtrack/badlapur-jeena-jeena-chords-1702994']
    scraper= AutoScraper()
    scraper.build(url, expected_output )
    search=request.GET['search']
    search_url='https://www.google.com/search?q=guitar+chords+of+song+{}'.format(search)
    search_results =scraper.get_result_similar(search_url)
    return render(request, 'search.html', {'data':search_results[0], 'search':search})
