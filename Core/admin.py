from django.contrib import admin
from Core.models import User, ErrorLog, HeadMenu, DropMenu, Label

# Register your models here.
admin.site.register(User)
admin.site.register(HeadMenu)
admin.site.register(DropMenu)
admin.site.register(ErrorLog)
admin.site.register(Label)