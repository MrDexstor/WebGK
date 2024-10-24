import requests
from Lib.LAN_check import server_avalible
from Core.AppSettings.config import BO_Url
from Lib import gk
from ServerAPI.session import session_check


@server_avalible('task_getActive')
@session_check
def getActive(request, only_count = False):
    
    if only_count:
        url = f'{BO_Url()}/api/tasks/active?onlyCount=true'
    else:
        url = f'{BO_Url()}/api/tasks/active'
    response = requests.get(url, headers=gk.getHeader(request.user))
    data ={}
    if response.status_code == 404:
        pass
    elif response.status_code == 401:
        pass
    elif response.status_code == 200:
        data = response.json()
    return data