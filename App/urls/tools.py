from django.urls import path, include
from App.tools import label


urlpatterns = [
    path('FPDD/', include('App.urls.toolsp.fpdd')),
    path('accessibility/', include('App.urls.toolsp.accessibility')),
    
    
    
    # Следующие ссылки требуется переместить по отдельным разделам
    path('labels/', label.label_list, name='label_list'),
    path('labels/load/', label.load_labels, name='load_labels'),
    path('labels/delete/', label.delete_labels, name='delete_labels'),
    path('labels/add/', label.add_label, name='add_label'),
    path('labels/print/', label.print_labels, name='print_labels'),
    path('labels/edit/', label.edit_label, name='edit_label'),
]