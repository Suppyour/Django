from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Front-End',
        'content': 'Контент в view'
    }
    return render(request, 'main/index.html', context)
def general(request):
    return HttpResponse('General Page')
