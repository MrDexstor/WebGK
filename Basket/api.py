from Basket import models
from Basket.tasks import update_basket

def getAllBasket():
    return models.Basket.objects.all()

class Basket:
    def __init__(self, basket_id):
        self.basket = models.Basket.objects.get(id = basket_id)
    def getItems(self):
        return models.BasketItem.objects.filter(basket = self.basket)
        
    def add(self, plu, quantity_in_basket): 
        item = models.BasketItem(plu= plu, quantity_in_basket = quantity_in_basket, basket= self.basket)
        item.save()
        
    def update(self):
        self.basket.state = 'locked'
        #self.basket.save()
        update_basket.delay(self.basket.id)
        
    def get_state(self):
        return self.basket.state