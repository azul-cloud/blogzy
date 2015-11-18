# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import main.models


class Migration(migrations.Migration):

    def populate_usernames(apps, schema_editor):
        User = apps.get_model("main", "User")

        for user in User.objects.all():
            if not user.username:
                user.username = user.email
                user.save()

    dependencies = [
        ('main', '0004_auto_20151118_1200'),
    ]

    operations = [
        migrations.RunPython(populate_usernames),
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=main.models.User.get_user_image_upload_path, null=True, blank=True),
            preserve_default=True,
        ),
    ]
