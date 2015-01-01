# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_type', models.CharField(max_length=1, choices=[(b'M', b'Monthly'), (b'B', b'Every 2 weeks'), (b'W', b'Weekly')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonalBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('logo', models.ImageField(null=True, upload_to=blog.models.get_blog_upload_path, blank=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('disqus', models.CharField(max_length=30, null=True, blank=True)),
                ('twitter', models.CharField(max_length=15, null=True, blank=True)),
                ('twitter_widget_id', models.CharField(max_length=18, null=True, blank=True)),
                ('facebook', models.CharField(max_length=40, null=True, blank=True)),
                ('instagram', models.CharField(max_length=40, null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=blog.models.get_post_upload_path)),
                ('image_description', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('headline', models.CharField(max_length=100, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.NullBooleanField(default=True)),
                ('views', models.IntegerField(default=0, editable=False, blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('lat', models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True)),
                ('long', models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True)),
                ('place_id', models.CharField(max_length=40, null=True, blank=True)),
                ('place', models.CharField(max_length=60, null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(to='blog.PersonalBlog')),
            ],
            options={
                'ordering': ['-create_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(to='blog.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserStreamBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_post_email', models.BooleanField(default=False)),
                ('email_newsletter', models.BooleanField(default=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(to='blog.PersonalBlog')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userstreamblog',
            unique_together=set([('user', 'blog')]),
        ),
        migrations.AlterUniqueTogether(
            name='userfavorite',
            unique_together=set([('user', 'post')]),
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(to='blog.Topic', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('blog', 'slug')]),
        ),
        migrations.AddField(
            model_name='blogsubscription',
            name='blog',
            field=models.ForeignKey(to='blog.PersonalBlog'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogsubscription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
