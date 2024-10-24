from Core.models import User
from Core.AppSettings.config import Service_Account
class service_account:
    def __init__(self):
        self.user = User.objects.get(id=Service_Account)

def service_api(funct, *args, **kwargs):
    request = service_account()
    return funct(request, *args,**kwargs)