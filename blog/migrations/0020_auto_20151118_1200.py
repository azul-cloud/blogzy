# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20151107_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalblog',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='personalblog',
            name='twitter_widget_id',
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='description',
            field=models.TextField(help_text='Tell us a bit about your blog and yourself'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='facebook',
            field=models.CharField(blank=True, max_length=40, help_text='Just the last part of your facebook URL (i.e. travelblogwave)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='twitter',
            field=models.CharField(blank=True, max_length=15, help_text="What is your Twitter handle? (Don't put @)", null=True),
            preserve_default=True,
        ),
    ]
