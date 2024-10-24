from django.urls import path, include
from App.page import basket

    
urlpatterns = [
    
    path('createb', basket.create, name='basket__create'),
    path('', basket.main, name='basket'),
    path('<str:id>/info//<str:pos>', basket.info, name='basket_info_z'),
    path('<str:id>/info/', basket.info, name='basket_info'),
    path('<str:id>/add/', basket.add),
    path('<str:id>/add/scan', basket.add_scan),
    path('<str:id>/bo_update', basket.update),
    
    
    
    
]