from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def test(request):
    print("Welcome to our site")
    return HttpResponse("<h1> This is Index Page<h1>")

def loginPage(request):
    return render(request, "login.html", {})

def signupPage(request):
    return render(request, "signup.html", {})
