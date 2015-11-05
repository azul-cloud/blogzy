# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20151104_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='active',
            new_name='public',
        ),
    ]
