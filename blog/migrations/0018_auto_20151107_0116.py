# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
