from Lib.UI import render


def main(request):
    return render(request, 'task_manager/index.html', 'Менеджер задач')