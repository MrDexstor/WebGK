from Lib.UI import render, redirect
from Scanner.Tools import BarcodeLoad
from Lib import session
from Scanner.windows import POSTerminal
from django.contrib import auth



def login(request):
    if request.method == 'POST':
        login_s = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(request, username=login_s, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
    return render(request, 'session/login.html', 'Авторизация в wGK', guest_mode=True, only_guest = True)
    
    
def auth_barcode(request):
    cfg = {'url': '/GK/session/auth/key'}
    return POSTerminal(request, cfg, guest = True)
    
    
def auth_token(request):
    call_barcode = BarcodeLoad(request.get_full_path())
    session.authenticate(request, call_barcode)
    return redirect('main')
    

def logout(request):
    auth.logout(request)
    return redirect('main')
    