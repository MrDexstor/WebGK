from django import shortcuts
from Core.models import Menu

def redirect(*args, **kwargs):
    return shortcuts.redirect(*args, **kwargs)
    
    
def render(request, template_name, title='', context={}, guest_mode=False):
    if guest_mode is False:
        if request.user.is_authenticated:
            context['GKRightMenu'] = Menu.objects.all()
        else:
            return redirect('main')
    
    
    context['title'] = title
    return shortcuts.render(request, template_name, context)
    
    
