from django.urls import path, include
from App.page import basket

    
urlpatterns = [
    # Страница со списком корзин
    path('', basket.main, name='basket'),
    # Система поиска позиций
    path('search/', basket.search_items, name='search_items'),
    path('search_page/', basket.search_page, name='search_page'),
    # Страница рабочего стола корзины
    path('<str:id>/', basket.info, name='basket_info'),
    # Страница создания корзины
    path('new_basket', basket.create, name='basket__create'),
    # API для функций корзины
    path('<str:basket_id>/items/', basket.basket_items),
    path('<int:basket_id>/item_add/', basket.basket_item_add, name='basket_item_add'),
    path('<int:basket_id>/item_delete/', basket.basket_item_delete, name='basket_item_delete'),
    path('<int:basket_id>/item_update/', basket.basket_item_update, name='basket_item_update'),
    # BackOffice:Синхронизация
    path('<str:id>/bo_update/', basket.update),
]
