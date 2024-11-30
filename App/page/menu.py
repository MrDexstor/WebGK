from Lib.page import Page, MasterMenu
from Lib.UI import render


def turnover(request):
    page = Page('Товарооборот', 'Товарооборот', 'Выполнение операций над товаром')
    menu = MasterMenu()
    menu.add('Информация о товаре', '/GK/items/', '/static/icon/colored/search.png')
    menu.add('Возвраты, отгрузка, перемещение товаров', '/GK/', '/static/icon/colored/logistic.png')
    menu.add('Локальная инвентаризация', '/GK/inventory/local/', '/static/icon/colored/inventory.png', '80')
    menu.add('Списания', '/GK/write-offs/', '/static/icon/colored/turnover.png', '80')
    menu.add('Уценка', '/GK/', '/static/icon/colored/low-price.png')
    menu.add('Корзины', '/GK/basket/', '/static/icon/colored/basket.png')
    return render(request, page, 'dm_style/menu/menu.html', {'menu': menu.build()})


def tools(request):
    page = Page('Инструменты', 'Инструменты', 'Обработчики для док-ов и задач')
    menu = MasterMenu()
    menu.add('Печать ценников', '/GK/', '/static/icon/colored/price-tag.png')
    menu.add('Печать этикеток (QR)', '/GK/tools/FPDD/', '/static/icon/colored/label.png')
    menu.add('Передача файлов', '/GK/', '/static/icon/colored/file-transfer.png')
    menu.add('Печать документа', '/GK/', '/static/icon/colored/print.png')
    menu.add('Фиктивная проводка документов доставки', '/GK/tools/FPDD/', '/static/icon/colored/storno.png', '80')
    menu.add('Доступность (Проводка)', '/GK/tools/accessibility/', '/static/icon/colored/accessibility.png', '0')
    menu.add('Сигналы УТП (Проводка)', '/GK/tools/YTP/', '/static/icon/colored/ytp.png', '6')
    return render(request, page, 'dm_style/menu/menu.html', {'menu': menu.build()})
    

def profile(request):
    page = Page('Профиль', 'Профиль')
    menu = MasterMenu()
    menu.add('Принтеры', '/GK/settings/',  '/static/icon/colored/printers.png')
    menu.add('WebGK AdminPanel', '/admin/', '/static/icon/colored/admin.png')
    menu.add('Выход', '', '/static/icon/colored/exit.png')

    return render(request, page, 'dm_style/menu/menu.html', {'menu': menu.build()})