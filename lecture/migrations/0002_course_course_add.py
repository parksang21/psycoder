# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
