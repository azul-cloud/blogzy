# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogsubscription_frequency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogsubscription',
            name='name',
        ),
    ]
