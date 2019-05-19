from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import process_utility
# Create your views here.

def index(request):
    return render(request,"index.html")


def process(request):
    url = request.POST['url']
    # return HttpResponse(process_utility.get_data(url))
    return render(request,"feeds.html",{"data":process_utility.get_data(url)})