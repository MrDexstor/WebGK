from django.urls import path, include
from api.ep import items

    
urlpatterns = [
    path('item', items.info),
]
