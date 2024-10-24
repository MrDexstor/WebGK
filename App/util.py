from django.http import HttpResponse
from ServerAPI.api import tasks

def dashboard_data_load(request):
    response = HttpResponse('''
    <html>
    <script>
        location.reload();
    </script>
    </html>
    ''')
    task_active = tasks.getActive(request, True)
    response.set_cookie("bo_TaskCount", task_active['tasksCount'], max_age=5)
    return response