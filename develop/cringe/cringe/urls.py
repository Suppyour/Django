"""
URL configuration for cringe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('general/',views.general, name = 'general'),
    path('index.html',views.index_html, name='index_html'),
    path('demand.html', views.demand, name='demand'),
    path('geography.html', views.geography, name='geography'),
    path('skills.html', views.skills, name='skills'),
]
