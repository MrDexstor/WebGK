import requests, json
from Lib.LAN_check import server_avalible
from Core.AppSettings.config import BO_Url
from Lib import gk
from ServerAPI.session import session_check
from datetime import datetime

@server_avalible('local_inv_getlist')
@session_check
def localGetList(request, code=''):
    url = f'{BO_Url()}/api/local-inventories?statusCodes=0,1,6,7'
    response = requests.get(url, headers=gk.getHeader(request.user))
    return response.json()
    
    
def createDoc(request, docName):
    url = f'{BO_Url()}/api/local-inventories'
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
    
    LIconf = {
        "creationDateTime":formatted_datetime,
        "name":docName
        
    }
    response = requests.post(url, headers=gk.getHeader(request.user), json=LIconf)
    
    return response.json()