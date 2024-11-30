from django.urls import path
from App.tools.task.accessibility import main


urlpatterns = [
    path('', main.main),
 #   path('<str:id>/', main.docPanel)
    
]