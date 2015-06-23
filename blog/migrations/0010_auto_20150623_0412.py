# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_personalblog_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsubscription',
            name='frequency',
            field=models.CharField(default='W', max_length=1, choices=[('W', 'Weekly'), ('M', 'Monthly')]),
            preserve_default=True,
        ),
    ]
