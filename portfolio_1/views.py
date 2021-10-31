from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.
def home(request):
    context={}
    return render(request, 'portfolio_1/home.html',context=context)