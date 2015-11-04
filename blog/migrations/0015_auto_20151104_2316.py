# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20151104_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='long',
            new_name='lng',
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=blog.models.get_blog_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
