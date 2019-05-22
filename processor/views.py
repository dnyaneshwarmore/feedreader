'''
This contains all the views required in processor app for scrapping the
input url.
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import process_utility
from . import constants
# Create your views here.

def index(request):
    """renders the home page"""
    return render(request,constants.INDEX_TEMPLATE)


def process(request):
    """processes the input url and sends the date  
    to web page for rendering
    """
    try:
        url = request.POST['url'].strip()
        title, data = process_utility.get_data(url)
        return render(request,constants.FEEDS_TEMPLATE, {"title":title,"data":data})
    except Exception as e:
        return render(request,constants.FEEDS_TEMPLATE,{"error":str(e)})