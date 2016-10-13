# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0002_auto_20161013_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_type', models.CharField(choices=[('1', 'gr'), ('2', 'lt'), ('3', 'pza'), ('4', 'box')], max_length=1)),
                ('stock', models.DecimalField(decimal_places=3, max_digits=9)),
                ('parent_metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Metric')),
            ],
        ),
        migrations.AddField(
            model_name='stockchain',
            name='metric',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='supplies.Metric'),
        ),
    ]
