import requests
from Lib.LAN_check import server_avalible
from Core.AppSettings.config import BO_Url
from Lib import gk
from ServerAPI.session import session_check


@server_avalible('print_labels')
@session_check
def print_labels(request, labels):
    url = f'{BO_Url()}/api/shelves/print'
    response = requests.get(url, headers=gk.getHeader(request.user), json=labels)
    