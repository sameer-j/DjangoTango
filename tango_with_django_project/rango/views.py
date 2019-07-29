
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says Hello!\
     <a style="float:right; padding:5px;" href="/rango/about">About</a>\
     <a style="float:right; padding:5px;" href="/">Tango Home</a>')

def about(request):
    return HttpResponse('You really ought to know about Rango, its awesome!\
     <a style="float:right; padding:5px;" href="/rango/">Home</a>\
     <a style="float:right; padding:5px;" href="/">Tango Home</a>')