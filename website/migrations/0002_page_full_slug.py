# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='full_slug',
            field=models.CharField(default='', editable=False, max_length=255),
            preserve_default=False,
        ),
    ]