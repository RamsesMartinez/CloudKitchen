# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0036_auto_20161028_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchoffice',
            old_name='addres',
            new_name='address',
        ),
    ]