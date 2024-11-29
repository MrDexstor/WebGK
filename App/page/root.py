from Lib.UI import render
from Lib import Log
from Lib.page import Page

def dashboard(request):
    if request.user.is_authenticated: 
        dash = Page('Дашбоард WebGK', 'Дашбоард', f'{request.user.name} ({request.user.storeRole})')
    else:
        dash = Page('Дашбоард WebGK', 'Дашбоард')
    return render(request, dash ,'dm_style/root/dashboard.html')