from django.urls import path, include

    
urlpatterns = [
    path('items/', include('api.endpoints.items')),
    
]
