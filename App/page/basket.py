from Lib.UI import render, redirect
from Basket import api, models
from Scanner.windows import POSTerminal
from Scanner.Tools import BarcodeLoad


def main(request):
    return render(request, 'basket/index.html', 'Корзины', {'baskets': api.getAllBasket()})
    
    
def info(request, id, pos = None):
    Basket = api.Basket(id)
    if Basket.get_state() == 'locked':
        return redirect('main')
    if pos == 's':
        return POSTerminal(request, POS_config={'url': f'/GK/basket/{id}/add/scan'})
    return render(request, 'basket/info.html', 'Корзина', {'items': Basket.getItems()}, POSScanner = True)
  
    
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