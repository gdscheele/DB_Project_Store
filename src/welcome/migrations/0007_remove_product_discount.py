# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20151120_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]
