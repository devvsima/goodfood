from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request) -> HttpResponse:
    context = {
        "title": 'EASY4U',
    }
    return render(request, 'main/index.html', context)

def info(request) -> HttpResponse:
    context = {
        "title": 'Про нас',
    }
    return render(request, 'main/info.html', context)

def contact(request) -> HttpResponse:
    context = {
        "title": 'Контакти',
    }
    return render(request, 'main/contact.html', context)
