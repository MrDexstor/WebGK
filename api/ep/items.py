from django.http import JsonResponse
from ServerAPI.api import items

def info(request):
    if request.method == 'GET':
        article = request.GET.get('article')
        responce = items.item__info(request, article)
        print(responce)
        return JsonResponse(responce)