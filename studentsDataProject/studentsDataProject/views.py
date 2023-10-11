from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def home(request):
    return HttpResponse("Welcome to our site")
def loginPage(request):
    return render(request, "login.html", {})

def signupPage(request):
    return render(request, "signup.html", {})
