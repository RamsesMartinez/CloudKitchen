# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0024_auto_20161024_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashregister',
            name='code',
            field=models.CharField(default='Dab', max_length=5),
        ),
    ]