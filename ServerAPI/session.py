from Core.models import User
from ServerAPI.api import sessions

def loginBO(request):
    account = User.objects.get(id=request.user.id)
    account.bearer_token = sessions.login(request)['accessToken']['value']
    account.save()


def session_check(funct):
    def wrapper(request, *args, **kwargs):
        loginBO(request)
        result = funct(request, *args, **kwargs)
        return result
    return wrapper