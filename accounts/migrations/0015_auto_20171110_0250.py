# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20171110_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='workplaces',
            new_name='workplace',
        ),
    ]