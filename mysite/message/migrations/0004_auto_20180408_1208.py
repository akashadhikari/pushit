# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 12:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fcm_django', '0003_auto_20170313_1314'),
        ('message', '0003_auto_20180408_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='CRM', max_length=255)),
                ('message', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, help_text='Admin notes.', null=True)),
                ('response_message', models.TextField(blank=True, help_text='FCM response.', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('last_sent_at', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='push_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('fcmdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fcm_django.FCMDevice')),
                ('device_type', models.CharField(choices=[('ANDROID', 'ANDROID')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('fcm_django.fcmdevice',),
        ),
        migrations.AlterField(
            model_name='message',
            name='select_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='message',
            name='select_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
