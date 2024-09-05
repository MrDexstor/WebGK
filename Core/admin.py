from django.contrib import admin
from Core.models import User, ErrorLog, Menu

# Register your models here.
admin.site.register(User)
admin.site.register(Menu)
admin.site.register(ErrorLog)