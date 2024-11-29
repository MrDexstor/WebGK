from django.urls import path, include


urlpatterns = [
    path('local/', include('App.urls.inventoryp.local'))
]
