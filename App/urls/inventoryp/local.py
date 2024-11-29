from django.urls import path
from App.page.inventory import local


urlpatterns = [
    path('', local.main),
    
]