# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGolf', '0005_auto_20170412_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangedrill',
            name='drill',
            field=models.CharField(choices=[('Extreme Miss', 'Extreme Miss'), ('Toe/Heel/Center Strike', 'Toe/Heel/Center Strike'), ('Toe/Heel Setup', 'Toe/Heel Setup'), ('Gate Strike', 'Gate Strike'), ('Toe or Heel Constraint', 'Toe or Heel Constraint')], default='Toe/Heel/Center Strike', max_length=40),
        ),
    ]
