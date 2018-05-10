from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os
import json

def index(request):
    return HttpResponse("hi")
def insta(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'instalinks.json')
    with open(file_path, 'r') as content:
        data= content.read()
    return JsonResponse(data, safe=False)

def fb(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'Postlinks.json')
    with open(file_path, 'r') as content:
        data= content.read()
    return JsonResponse(data, safe=False)

def youtube(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'Videolinks.json')
    with open(file_path, 'r') as content:
        data= content.read()
    return JsonResponse(data, safe=False)

def tweet(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'Tweetlinks.json')
    with open(file_path, 'r') as content:
        data= content.read()
    return JsonResponse(data, safe=False)

def news(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'links.json')
    with open(file_path, 'r') as content:
        data= content.read()
    return JsonResponse(data, safe=False)
# Create your views here.
