# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0026_auto_20161024_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchoffice',
            name='manager',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
    ]
