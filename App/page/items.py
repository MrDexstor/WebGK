import json
from GKC.settings import BASE_DIR
from Lib.UI import render, redirect
from ServerAPI.api import items
from Scanner.windows import POSTerminal
from Scanner.Tools import BarcodeLoad


def item_info(request, plu):
    item = items.item__info(request, plu)
    return render(request, 'items/item_info.html', 'Информация о товаре', {"item": item})
   
   
def item_movements(request, plu):
    item = items.item__movements(request, plu)
    return render(request, 'items/item_movements.html', 'Информация о товаре', {"item": item})


def item_plg(request, plu):
    item = items.item__plg(request, plu)
    return render(request, 'items/item_plg.html', 'Информация о товаре', {"item": item})

  
def search(request, pos = None):
    if pos is None:
        if request.method == 'POST':
            article = request.POST.get('plu', None)
            nameContains = request.POST.get('item_name', None)
            limit = request.POST.get('max-position', None)
            # Запросить из системы данные 
            sr_result = items.search(request, itemIds= article, nameContains=nameContains, limit = limit)
            if len(sr_result) == 1:
                return redirect(f'/GK/items/item/{ sr_result[0]['article'] }/info')
            elif len(sr_result) == 0:
                return render(request, 'items/search.html', 'Поиск товара', POSScanner = True)
            else: 
                return render(request, 'items/search_result.html', 'Поиск товара', {'items': sr_result})
        else:
            return render(request, 'items/search.html', 'Поиск товара', POSScanner = True)
    elif pos == 's':
        try:
            article = request.GET['barcode']
        except Exception:
            article = None
        else:
            article = True
            
            
        if article is None:
            return POSTerminal(request, POS_config={'url': '/GK/items//s'})
        else:
            barcode = BarcodeLoad(request.get_full_path())
            sr_result = items.search(request, itemIds= barcode)
            if len(sr_result) == 1:
                return redirect(f'/GK/items/item/{ sr_result[0]['article'] }/info')
            elif len(sr_result) == 0:
                return render(request, 'items/search.html', 'Поиск товара', POSScanner = True)
            else: 
                return render(request, 'items/search_result.html', 'Поиск товара', {'items': sr_result})