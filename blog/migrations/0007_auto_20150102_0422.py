# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150102_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsubscription',
            name='frequency',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'W', b'Weekly'), (b'M', b'Monthly')]),
            preserve_default=True,
        ),
    ]
