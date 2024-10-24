from Lib.UI import render
from Core.AppSettings.config import Root_Url


def POSTerminal(request, POS_config={}, guest = False):
    POS_config['root'] = Root_Url
    if guest is False:
        background = 'Core/base_layer.html'
    else:
        background = 'Core/blank_layer.html'
        
    return render(request, 'POS/terminal.html', 'Сканирование', {'POS_cfg': POS_config, 'background': background}, guest_mode = guest, only_guest = guest)