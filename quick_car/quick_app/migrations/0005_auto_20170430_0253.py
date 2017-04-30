# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-29 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quick_app', '0004_auto_20170430_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
        migrations.AddField(
            model_name='user',
            name='notification',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quick_app.Notification'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='to_user',
            field=models.CharField(max_length=100),
        ),
    ]
