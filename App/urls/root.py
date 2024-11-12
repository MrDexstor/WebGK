from django.contrib import admin
from django.urls import path, include
from App.page import root, session

    
urlpatterns = [
    path('', root.dashboard , name='main'),
    path('session/', include('App.urls.session')),
    path('items/', include('App.urls.items')),
    path('task-manager/', include('App.urls.task')),
    path('basket/', include('App.urls.basket')),
    path('tools/', include('App.urls.tools')),
]
