from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

def index(request):
    num_visits = request.session.get('num_visits', 0)
    context={num_visits:'num_visits'}
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