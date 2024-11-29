from django.urls import path
from App.page import menu


urlpatterns = [
    path('turnover/', menu.turnover),
    path('profile/', menu.profile),
    path('tools/', menu.tools)
]
