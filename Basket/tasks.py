from celery import shared_task
import json
from time import sleep
from django.shortcuts import get_object_or_404
from .models import Basket, BasketItem
from ServerAPI.api.items import item__info
from ServerAPI.service_tech import service_api

@shared_task
def update_basket(basket_id):
    basket = BasketItem.objects.filter(basket=basket_id)
    items_to_delete = []
    
    # Перебираем все товары в корзине
    for basket_item in basket:
        plu = basket_item.plu
        response = service_api(item__info, basket_item.plu)

        if response:
            # Обновляем данные товара
            data = response
            print(f'Запрашивается ирформация по товару (10 сек): {basket_item}')
            
            if data['article']:
                basket_item.name = data.get('shortName', '')
                basket_item.stock_quantity = data.get('stock', '')
                basket_item.plu = data.get('article', plu)
                basket_item.save()
            else:
                items_to_delete.append(basket_item.id)
        else:
            items_to_delete.append(basket_item.id)

    BasketItem.objects.filter(id__in=items_to_delete).delete()

    # Проверяем наличие дублирующихся PLU и объединяем их
   # consolidate_duplicate_plu(basket)

def consolidate_duplicate_plu(basket):
    plu_dict = {}

    # Сначала собираем все товары по PLU
    for basket_item in basket.basketitem_set.all():
        plu = basket_item.plu
        if plu in plu_dict:
            plu_dict[plu]['quantity_in_basket'] += int(basket_item.quantity_in_basket)
            plu_dict[plu]['stock_quantity'] += int(basket_item.stock_quantity)
        else:
            plu_dict[plu] = {
                'name': basket_item.name,
                'quantity_in_basket': int(basket_item.quantity_in_basket),
                'stock_quantity': int(basket_item.stock_quantity),
                'basket_item': basket_item
            }

    # Удаляем все текущие записи и создаем новые
    basket.basketitem_set.all().delete()
    for plu, data in plu_dict.items():
        BasketItem.objects.create(
            plu=plu,
            name=data['name'],
            quantity_in_basket=data['quantity_in_basket'],
            stock_quantity=data['stock_quantity'],
            basket=basket
        )

# Пример использования
# update_basket_items(basket_id)
