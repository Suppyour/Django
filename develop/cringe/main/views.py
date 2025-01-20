from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Front-End',
        'content': "Front-End разработка"
    }
    return render(request, 'main/index.html', context)

def general(request):
    context: dict = {
        'title': 'Общее',
        'content': "Общая информация",
        'text_on_page': "Какой то текст"
    }
    return render(request, 'main/general.html', context)

def index_html(request):
    context: dict = {
        'title': 'Front-End',
        'content': "Front-End разработка"
    }
    return render(request, 'main/index.html', context)

def demand(request):
    context: dict = {
        'title': 'Востребованность',
        'content': "Front-End разработка"
    }
    return render(request, 'main/demand.html', context)

def geography(request):
    context: dict = {
        'title': 'География',
        'content': "Front-End разработка"
    }
    return render(request, 'main/geography.html', context)

def skills(request):
    context: dict = {
        'title': 'Навыки',
        'content': "Front-End разработка"
    }
    return render(request, 'main/skills.html', context)