# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogsubscriptionlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalblog',
            name='logo',
        ),
    ]
