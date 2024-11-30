from Lib.page import Page
from Lib.UI import render


def main(request):
    page = Page('Доступность WGK', 'Доступность', 'Данные позиции не продаются')
    page.returnUrl(request.META.get('HTTP_REFERER'))
    return render(request, page, 'tools/accessibility/main.html')