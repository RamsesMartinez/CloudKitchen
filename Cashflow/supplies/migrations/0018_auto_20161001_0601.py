# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 11:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0017_auto_20161001_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='barcode',
            field=models.PositiveIntegerField(blank=True, help_text='(Código de barras de 13 digitos)', null=True, validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AlterField(
            model_name='supply',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='supply',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
