# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20160417_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalblog',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=500, help_text='Tell us a bit about your blog and yourself'),
            preserve_default=True,
        ),
    ]
