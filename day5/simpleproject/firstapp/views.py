from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to django</h1>")

def welcome(request):
    return HttpResponse("<h1>Another response from django app</h1>")