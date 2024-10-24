from django.contrib import admin
from django.urls import path, include
from App.page import session

    
urlpatterns = [
    path('auth/key', session.auth_token),
    path('', session.login, name='login'),
    path('auth/scan', session.auth_barcode, name='auth_scan'),
    path('logout', session.logout)
]
