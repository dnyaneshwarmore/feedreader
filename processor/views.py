'''
This contains all the views required in processor app for scrapping the
input url.
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import  process_utility
# Create your views here.

def index(request):
    """renders the home page"""
    return render(request,"index.html")


def process(request):
    """processes the input url and sends the date  
    to web page for rendering
    """
    url = request.POST['url']
    title, data = process_utility.get_data(url)
    return render(request,"feeds.html",{"title":title,"data":data})