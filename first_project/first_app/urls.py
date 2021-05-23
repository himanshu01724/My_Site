from django.urls import include
from django.urls.conf import include,path
from first_app import views

URLPattern = [
    path('first_app/',views.index,name='index'),
]