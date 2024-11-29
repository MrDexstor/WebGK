from django.contrib import admin
from django.urls import path, include
from App.page import root, session
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('', root.dashboard , name='main'),
    path('session/', include('App.urls.session')),
    path('items/', include('App.urls.items')),
    path('task-manager/', include('App.urls.task')),
    path('basket/', include('App.urls.basket')),
    path('tools/', include('App.urls.tools')),
    path('inventory/', include('App.urls.inventory')),
    path('menu/', include('App.urls.menu')),
    path('file_transfer/', include('TransferFile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

