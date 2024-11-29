from django.urls import path
from App.tools.fpdd import main


urlpatterns = [
    path('', main.main),
    path('<str:id>/', main.docPanel)
    
]