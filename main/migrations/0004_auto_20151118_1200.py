# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151107_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='user',
            name='twitter',
        ),
    ]
