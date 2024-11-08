from Lib.UI import render, redirect
from Basket import api, models
from Scanner.windows import POSTerminal
from Scanner.Tools import BarcodeLoad
from django.http import JsonResponse
from Basket.models import BasketItem, Basket
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from ServerAPI.api.items import search

def search_items(request):
    itemIds = request.GET.get('itemIds')
    nameContains = request.GET.get('nameContains')
    tradeGroup = request.GET.get('tradeGroup')
    limit = request.GET.get('limit')

    data = search(request, itemIds, nameContains, tradeGroup, limit)
    return JsonResponse(data, safe=False)



def search_page(request):
    return render(request, 'Core/search.html')


def main(request):
    return render(request, 'basket/index.html', 'Корзины', {'baskets': api.getAllBasket()})
    
    
def info(request, id):
    basket = Basket.objects.get(id=id)
    return render(request, 'basket/info.html', 'Корзина', {'basket': basket})
  

def basket_items(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)
    items = BasketItem.objects.filter(basket=basket)
    items_data = [
        {
            'id': item.id,
            'plu': item.plu,
            'name': item.name,
            'quantity_in_basket': item.quantity_in_basket,
            'stock_quantity': item.stock_quantity,
        }
        for item in items
    ]
    return JsonResponse(items_data, safe=False)    
    
@csrf_exempt
def basket_item_add(request, basket_id):
    if request.method == 'POST':
        basket = get_object_or_404(Basket, id=basket_id)
        plu = request.POST.get('plu')
        quantity_in_basket = request.POST.get('quantity_in_basket')
        BasketItem.objects.create(
            plu=plu,
            name='',
            quantity_in_basket=quantity_in_basket,
            stock_quantity='',
            basket=basket
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def basket_item_delete(request, basket_id):
    if request.method == 'POST':
        basket = get_object_or_404(Basket, id=basket_id)
        item_ids = request.POST.getlist('item_ids[]')
        print(item_ids)
        BasketItem.objects.filter(id__in=item_ids, basket=basket).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
    
    
    
    
    
def add(request, id):
    if request.method == 'POST':
        Basket = api.Basket(id)
        plu = request.POST.get('plu')
        quantity_in_basket = request.POST.get('quantity_in_basket')
        if plu and quantity_in_basket:
            Basket.add(plu, quantity_in_basket)
    return redirect(f'/GK/basket/{id}/info')
    
    
def add_scan(request, id):
    Basket = api.Basket(id)
    plu = BarcodeLoad(request.get_full_path())
    if plu:
        Basket.add(plu, 0)
    return redirect(f'/GK/basket/{id}/info')
    
    
def update(request, id):
    Basket = api.Basket(id)
    Basket.update()
    return redirect('main')
    
    
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name', None) 
        if name is not None:
            Basket = models.Basket(name=name)
            Basket.save()
        return redirect('/basket')
    else:
        return render(request, 'basket/create.html', 'Создание корзины')