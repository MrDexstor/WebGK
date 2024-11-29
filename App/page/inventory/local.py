from Lib.UI import render
from Lib.page import Page
from ServerAPI.api.local_inventories import localGetList


def main(request):
    li = localGetList(request, '0,1,6,7')
    page = Page('Локальные инвентаризации', 'Локальные инвентаризации', 'Список всех открытых/созданных ЛИ')
    page.returnUrl(request.META.get('HTTP_REFERER'))
    return render(request, page, 'inventory/local/list.html', {'li': li})