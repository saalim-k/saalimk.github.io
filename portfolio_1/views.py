from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context=context)

def home(request):
    context={}
    return render(request, 'home.html',context=context)

def portfolio(request):
    context={}
    return render(request,'portfolio_1/portfolio.html',context=context)

def about(request):
    context={}
    return render(request,'portfolio_1/about.html',context=context)