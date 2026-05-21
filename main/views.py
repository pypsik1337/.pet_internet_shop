

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Home',
        'content' : 'Главная страница магазина',
        'list' : ['first', 'second'],
        'dict' : {'first' : 1},
        'bool' : True
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('about page')
