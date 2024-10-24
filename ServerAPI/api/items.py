import requests
from Lib.LAN_check import server_avalible
from Core.AppSettings.config import BO_Url
from Lib import gk
from ServerAPI.session import session_check
from Lib.Tools import text_codec

@server_avalible('item__info')
@session_check
def item__info(request, plu, info_level='deep'):
    if info_level == 'deep':
        url = f'{BO_Url()}/api/item?itemId={plu}&expand=itemIds%2CnextIncoming%2ClabelPrintingAllowed%2CassortmentPrintingAllowed%2CpriceTagPrintingAllowed%2CthirtyDaysAvgSales%2CcreateMarkdownAllowed%2CthirtyDaysSumWriteOff%2ClayoutsForMobilePrinter%2CitemAllowedForSale%2CcreateMarkableMarkdownWithoutDatamatrix%2CdefaultLayoutForMobilePrinter'
    elif info_level == 'search':
        pass
    elif info_level == 'min':
        pass
    else:
        pass
    
    response = requests.get(url, headers=gk.getHeader(request.user))
    data ={}
    if response.status_code == 404:
        pass
    elif response.status_code == 401:
        pass
    elif response.status_code == 200:
        data = response.json()
    return data
    
   
@server_avalible('item__movements')
@session_check
def item__movements(request, plu):
    url = f'{BO_Url()}/api/item/{plu}/movements'
    response = requests.get(url, headers=gk.getHeader(request.user))
    data ={}
    if response.status_code == 404:
        pass
    elif response.status_code == 401:
        pass
    elif response.status_code == 200:
        data = response.json()
    return data


@server_avalible('item__plg')
@session_check
def item__plg(request, plu):
    url = f'{BO_Url()}/api/item/{plu}/planogram'
    response = requests.get(url, headers=gk.getHeader(request.user))
    data ={}
    if response.status_code == 404:
        pass
    elif response.status_code == 401:
        pass
    elif response.status_code == 200:
        data = response.json()
    return data
    
    
@server_avalible('item__search')
@session_check
def search(request,  itemIds= None, nameContains= None, tradeGroup = None ,limit = None):
    url = f'{BO_Url()}/api/items'
    # Преобразование переменных
    if itemIds == '':
        itemIds = None
    if nameContains == '':
        nameContains = None
    if tradeGroup == '':
        tradeGroup = None
    if limit == '':
        limit = None
    # Обратотка переменных
    search_filter = {}
    if itemIds is not None:
        search_filter['itemIds'] = itemIds
    if nameContains is not None:
        search_filter['nameContains'] = text_codec(nameContains)
    if limit is not None:
        search_filter['limit'] = limit
    else:
        search_filter['limit'] = 15
    # Обработка запроса
    response = requests.get(url, headers=gk.getHeader(request.user), params = search_filter)
    data ={}
    if response.status_code == 404:
        pass
    elif response.status_code == 401:
        pass
    elif response.status_code == 200:
        data = response.json()
    return data