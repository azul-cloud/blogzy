# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20151026_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalblog',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=blog.models.get_post_upload_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(related_name='posts', to='blog.PersonalBlog'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
            preserve_default=True,
        ),
    ]
