# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='items',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='menus.Menu'),
            preserve_default=False,
        ),
    ]
