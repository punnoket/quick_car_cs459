# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-06 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quick_app', '0009_mechanic_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
