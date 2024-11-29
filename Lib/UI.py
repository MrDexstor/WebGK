from django import shortcuts
from Core.AppSettings import config
from Lib.ServerTools import BuilderMenu
from App import util


def redirect(*args, **kwargs):
    return shortcuts.redirect(*args, **kwargs)
    
    
def render(request, page_conf, template_name, context={}, POSScanner = False, guest_mode=False, only_guest=False):
    
    if config.Cookie_WorkerEnabled is True and guest_mode is False and request.user.is_authenticated:
        try:
            cookie_TaskCount = request.COOKIES["bo_TaskCount"] 
        except KeyError:
            return util.dashboard_data_load(request)
        else:
            context['bo_TaskCount'] = str(cookie_TaskCount)
    elif request.user.is_authenticated is False:
        redirect('login')
    
    if guest_mode is False:
        only_guest = False
    
    if only_guest and request.user.is_authenticated : 
        return redirect('main')
        
        
    if guest_mode is False:
        if request.user.is_authenticated:
            context['GKRightMenu'] = BuilderMenu(request)
            if config.POS_ScannerAllowed:
                if POSScanner is True:
                    context['POSScanner'] = request.get_full_path() + '/s'
                else:
                   try:
                       context['POSScanner']
                   except Exception:
                       pass
                   else:
                       del context['POSScanner']
        else:
            return redirect('login')
    
    context['page'] = page_conf.build()
    return shortcuts.render(request, template_name, context)
    
    
