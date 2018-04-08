from django.contrib import admin
from .models import Message, UserDevice, PushMessage

# Register your models here.

admin.site.register(Message)
admin.site.register(UserDevice)
admin.site.register(PushMessage)