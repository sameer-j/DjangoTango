from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello. You are at Polls App.\
     <a style="float:right; padding:5px;" href="/">Django Home</a>')

