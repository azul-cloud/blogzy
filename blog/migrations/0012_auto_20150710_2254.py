# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_personalblog_disqus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=blog.models.get_post_upload_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='place',
            field=models.CharField(max_length=100, blank=True, null=True),
            preserve_default=True,
        ),
    ]
