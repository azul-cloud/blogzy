# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150710_2254'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blogsubscription',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='blogsubscription',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blogsubscriptionlog',
            name='subscription',
        ),
        migrations.DeleteModel(
            name='BlogSubscription',
        ),
        migrations.DeleteModel(
            name='BlogSubscriptionLog',
        ),
        migrations.AlterUniqueTogether(
            name='userfavorite',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userfavorite',
            name='post',
        ),
        migrations.RemoveField(
            model_name='userfavorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFavorite',
        ),
        migrations.AlterUniqueTogether(
            name='userstreamblog',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userstreamblog',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='userstreamblog',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserStreamBlog',
        ),
    ]
