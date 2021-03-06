# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBGolf', '0008_auto_20170414_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChipDrill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('club', models.CharField(max_length=10)),
                ('balls_hit', models.IntegerField()),
                ('balls_ontarget', models.IntegerField()),
                ('drill', models.CharField(choices=[('Home Mat Chip', 'Home Mat Chip'), ('Close Hole Chip', 'Close Hole Chip'), ('Far Hole Chip', 'Far Hole Chip'), ('Lob Shot', 'Lob Shot'), ('Bump and Run', 'Bump and Run'), ('Bunker Shot', 'Bunker Shot')], default='Home Mat Chip', max_length=40)),
            ],
        ),
    ]
