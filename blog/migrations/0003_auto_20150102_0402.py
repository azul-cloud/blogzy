# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogsubscription',
            name='sub_type',
        ),
        migrations.RemoveField(
            model_name='blogsubscription',
            name='user',
        ),
        migrations.AddField(
            model_name='blogsubscription',
            name='email',
            field=models.EmailField(default='noreply@nodomain.com', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogsubscription',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
