# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGolf', '0004_rangedrill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangedrill',
            name='drill',
            field=models.CharField(choices=[('FS1', 'Toe/Heel/Center Strike'), ('FS2', 'Toe/Heel Setup')], default='FS1', max_length=40),
        ),
    ]