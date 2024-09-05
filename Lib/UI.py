from django import shortcuts


def render(request, template_name, title='', context={}):
    context['title'] = title
    return shortcuts.render(request, template_name, context)
    
    
def redirect(*args, **kwargs):
    return shortcuts.redirect(*args, **kwargs)