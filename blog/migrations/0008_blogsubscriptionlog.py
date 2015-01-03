# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150102_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSubscriptionLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_date_time', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.ForeignKey(to='blog.BlogSubscription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
