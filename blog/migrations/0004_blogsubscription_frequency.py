# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150102_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsubscription',
            name='frequency',
            field=models.CharField(default=b'W', max_length=1),
            preserve_default=True,
        ),
    ]
