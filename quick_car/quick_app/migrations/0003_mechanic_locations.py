# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-29 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quick_app', '0002_mechanic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='locations',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
