# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='docuents/'),
        ),
    ]
