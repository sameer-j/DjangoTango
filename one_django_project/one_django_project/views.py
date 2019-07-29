from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>One Django Home</h1>\
    <ul>\
    <li><a href="/rango/">rango</a></li>\
    <li><a href="/polls/">polls</a></li>\
    </ul>')