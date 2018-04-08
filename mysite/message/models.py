from django.db import models
from fcm_django.models import FCMDevice
from django.contrib.auth.models import User, Group


class Message(FCMDevice):
	text_message = models.CharField(max_length=255, null=True, blank=True)
	select_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	select_group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)


class UserDevice(FCMDevice):
    TYPES = (
        ('ANDROID', 'ANDROID'),
        # ('IOS', 'IOS'),
    )
    auth_user = models.ForeignKey(User, related_name='devices', null=True, blank=True)
    device_type = models.CharField(choices=TYPES, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def send_all(cls, msg):
        cls.objects.filter(is_active=True).send_message(msg)

    def __str__(self):
        return 'FCM Device for %s' % self.auth_user


class PushMessage(models.Model):
    title = models.CharField(max_length=255, default='CRM')
    message = models.TextField()
    url = models.URLField(blank=True, null=True)
    remarks = models.TextField(null=True, blank=True, help_text='Admin notes.')
    response_message = models.TextField(null=True, blank=True, help_text='FCM response.')
    author = models.ForeignKey(User, related_name='push_messages', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    last_sent_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        # truncate to 75 chars
        char_len = 75
        return (self.message[:char_len] + '..') if len(self.message) > char_len else self.message

    def send(self):
        response = UserDevice.objects.filter(is_active=True).send_message(
            {'type': 'message', 'message': self.message, 'title': self.title, 'url': self.url})
        self.response_message = response
        self.last_sent_at = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
        self.save()