from django.db import models
from django.utils import timezone


class Basket(models.Model):
    name = models.CharField('Наименование корзины', unique=True, max_length=100)
    created = models.DateTimeField('Дата и время создания', default= timezone.now)
    state = models.CharField('Состояние корзины', max_length=100, default='in_work')
#################
# in_work - в работе
# locked - заблокирование,ожидание обработки
#################
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    def __str__(self):
        return self.name
        
        
class BasketItem(models.Model):
    plu = models.CharField('PLU', max_length=100)
    name = models.CharField('Наименование товара', max_length=100)
    quantity_in_basket = models.CharField('Количество в корзине', max_length=100)
    stock_quantity = models.CharField('Остаток на момент добавление', max_length=100)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.plu