# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-30 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quick_app', '0007_auto_20170501_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='notification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quick_app.Notification'),
        ),
    ]
