# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2024-04-20 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
