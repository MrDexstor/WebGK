from django.urls import path, include
from Scanner.windows import POSTerminal

urlpatterns = [
    path('', POSTerminal),

    
]
