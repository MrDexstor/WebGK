import json, requests
from GKC.settings import BASE_DIR
from Core.AppSettings.config import BO_Url


def server_avalible(funct_name):
    def server_avalible_checker(function):
        def wrapper(*args, **kwargs):
            try:
                 requests.get(f'{BO_Url()}/ping')
            except Exception:
                result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json'))
            else:
                result = function(*args, **kwargs)
            return result
        return wrapper
    return server_avalible_checker