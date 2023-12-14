from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def home(req):
    return render(req, "home.html")

def logout_view(req):
    logout(req)
    return redirect("/")