# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('fcm', '0002_device_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='dev_id',
            field=models.CharField(max_length=50, verbose_name='Device ID', unique=True),
        )
    ]
