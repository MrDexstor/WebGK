from django.contrib.auth import login
from Core.models import User


def authenticate(request, token):
    auth_log = {}
    try:
        userX = User.objects.get(login_key=token)
    except User.DoesNotExist:
        auth_log['message'] = 'Пользователь не найден'
    else:
        return login(request, userX)