# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 01:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_invite_email_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='email_sent',
        ),
    ]
