# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 01:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0004_auto_20170219_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]