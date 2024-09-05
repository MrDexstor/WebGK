from Lib.UI import render
from Lib import Log

def dashboard(request):
    return render(request, 'root/dashboard.html', 'Рабочий стол')