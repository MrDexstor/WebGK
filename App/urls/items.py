from django.contrib import admin
from django.urls import path, include
from App.page import items

    
urlpatterns = [
    path('', items.search, name='item_search'),
    path('/<str:pos>', items.search, name='item_search_s'),
    path('item/<str:plu>/info', items.item_info, name='item_info'),
    path('item/<str:plu>/movements', items.item_movements, name='item_movements'),
    path('item/<str:plu>/plg', items.item_plg, name='item_plg'),
    path('item/<str:plu>/datamatrix', items.item_datamatrix, name='item_datamatrix'),
]
