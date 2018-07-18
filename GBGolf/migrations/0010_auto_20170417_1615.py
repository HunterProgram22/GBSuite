# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGolf', '0009_chipdrill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chipdrill',
            name='drill',
            field=models.CharField(choices=[('Home Mat Chip', 'Home Mat Chip'), ('Close Hole Chip', 'Close Hole Chip'), ('Far Hole Chip', 'Far Hole Chip'), ('Lob Shot', 'Lob Shot'), ('Bump and Run', 'Bump and Run'), ('Bunker Shot', 'Bunker Shot'), ('3 Coin Chip', '3 Coin Chip')], default='Home Mat Chip', max_length=40),
        ),
    ]