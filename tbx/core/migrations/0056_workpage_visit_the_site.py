# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0055_auto_20160830_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='visit_the_site',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]