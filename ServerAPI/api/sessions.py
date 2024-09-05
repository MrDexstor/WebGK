import requests
from Lib import gk,Log


def login(request):
    url = gk.point('login')
    
    response = requests.get(url, headers=gk.getHeader(request.user, True))
        
    if response.status_code == 200:
        return response.json()
    else:
        Log.register(f'При запросе к "{url}" произошла ошибка с кодом {response.status_code}')