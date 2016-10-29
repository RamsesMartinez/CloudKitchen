# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0038_auto_20161028_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PR', 'Provider'), ('ST', 'Stock'), ('AS', 'Assembled'), ('SO', 'Sold')], default='PR', max_length=15)),
                ('metric', models.CharField(choices=[('GR', 'gramo'), ('LI', 'litro'), ('PI', 'pieza'), ('PA', 'paquete'), ('BO', 'caja')], default='GR', max_length=10)),
                ('cartridge_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplies.Cartridge')),
                ('supply', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='supplies.Supply')),
            ],
            options={
                'verbose_name': 'Stock Chain',
                'verbose_name_plural': 'Stocks Chain',
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='cartridge_id',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='supply',
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('id',), 'verbose_name': 'Ticket Details', 'verbose_name_plural': 'Tickets Details'},
        ),
        migrations.RemoveField(
            model_name='branchoffice',
            name='address',
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='addres',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]