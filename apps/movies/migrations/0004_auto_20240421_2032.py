# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2024-04-22 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20240419_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AlterField(
            model_name='movies',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Categories', verbose_name='Especialidad'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.CharField(max_length=256, verbose_name='Teléfono'),
        ),
    ]
