# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170711_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='full_slug',
            field=models.CharField(default=None, editable=False, max_length=255),
            preserve_default=False,
        ),
    ]