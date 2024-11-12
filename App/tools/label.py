from Lib.UI import render
from Core.models import Label
from App.tools.forms import LabelForm
from django.http import JsonResponse
from ServerAPI.api import printer

def label_list(request):
    labels = Label.objects.filter(user=request.user)
    form = LabelForm()
    return render(request, 'tools/label_list.html','Печать полок', {'labels': labels, 'form': form})

def load_labels(request):
    labels = Label.objects.filter(user=request.user).values('id', 'name', 'qr', 'appName', 'printer')
    return JsonResponse(list(labels), safe=False)

def delete_labels(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('item_ids[]')
        Label.objects.filter(id__in=item_ids, user=request.user).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def add_label(request):
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.user = request.user
            label.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})

def print_labels(request):
    if request.method == 'POST':
        selected_labels = request.POST.getlist('item_ids[]')
        labels = Label.objects.filter(id__in=selected_labels, user=request.user)
        label_data = []
        for label in labels:
            label_data.append({
                'name': label.name,
                'qr': label.qr,
                'appName': label.appName,
                'printer': label.printer
            })
        response = printer.print_labels(request, label_data)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def edit_label(request):
    if request.method == 'POST':
        label_id = request.POST.get('label_id')
        label = Label.objects.get(id=label_id, user=request.user)
        form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})