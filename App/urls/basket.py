from django.urls import path, include
from App.page import basket

    
urlpatterns = [
    
    path('createb', basket.create, name='basket__create'),
    path('', basket.main, name='basket'),
#    path('<str:id>/info//<str:pos>', basket.info, name='basket_info_z'),
    path('<str:id>/info/', basket.info, name='basket_info'),
    path('<str:id>/add/', basket.add),
    path('<str:id>/add/scan', basket.add_scan),
    path('<str:id>/bo_update', basket.update),
    path('<str:basket_id>/items/', basket.basket_items),
    path('<int:basket_id>/item_add/', basket.basket_item_add, name='basket_item_add'),
    path('<int:basket_id>/item_delete/', basket.basket_item_delete, name='basket_item_delete'),
    path('search/', basket.search_items, name='search_items'),
    path('search_page/', basket.search_page, name='search_page'),
]
