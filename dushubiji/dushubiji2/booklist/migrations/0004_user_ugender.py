# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0003_auto_20171116_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ugender',
            field=models.CharField(default='female', max_length=50),
        ),
    ]
