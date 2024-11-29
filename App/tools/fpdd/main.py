from Lib.page import Page
from Lib.UI import render
from ServerAPI.api import write_offs


def main(request):
    doc = write_offs.getList(request)
    page = Page('FDPP | WebGK', 'Документы списаний ЭД', 'Приемка и утилизация товаров')
    page.returnUrl('/GK/menu/tools/')
    return render(request, page, 'tools/fpdd/main.html', {"offs": doc})
    
def docPanel(request, id):
    doc = write_offs.offsData(request, id)
    write_offs_positions = write_offs.positions(request, doc["id"])
    page = Page('FDPP | WebGK', 'Списание товара доставки', f'{doc["docNumber"]}')
    page.returnUrl('/GK/tools/FPDD/')
    return render(request, page, 'tools/fpdd/info.html', {"off": doc, "positions": write_offs_positions})
    
 
def createLocal(request, id):
    writeoffs = write_offs.offsData(request, id)
    
    #2. Создать ЛИ с определёнными данными
    #3. Добавить позиции
    