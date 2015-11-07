# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20151107_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topics',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(null=True, max_length=100, help_text="100 characters to catch reader's attention", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=blog.models.get_post_upload_path, help_text='main image for your article'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image_description',
            field=models.CharField(max_length=100, help_text='What is your image? (ex: San Andres Beach Colombia)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False, help_text='Should the article be publically viewable now?'),
            preserve_default=True,
        ),
    ]
