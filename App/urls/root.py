from django.contrib import admin
from django.urls import path, include
from App.page import root

    
urlpatterns = [
    path('', root.dashboard , name='main'),
]
