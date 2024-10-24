from django.urls import path
from App.page import task_manager


urlpatterns = [
    path('', task_manager.main),
    
]
