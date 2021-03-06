# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0007_auto_20180515_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooler',
            name='controlmode',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Autom', 'Autom')], default='Autom', max_length=10),
        ),
        migrations.AlterField(
            model_name='cooler',
            name='fan',
            field=models.CharField(choices=[('Off', 'Off'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Off', max_length=10),
        ),
        migrations.AlterField(
            model_name='cooler',
            name='powermode',
            field=models.CharField(choices=[('On', 'On'), ('Off', 'Off'), ('Schedule', 'Schedule')], default='Schedule', max_length=10),
        ),
    ]
