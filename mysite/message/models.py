from django.db import models
from fcm_django.models import FCMDevice
from django.contrib.auth.models import User, Group


class Message(FCMDevice):
	text_message = models.CharField(max_length=255, null=True, blank=True)
	select_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	select_group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
