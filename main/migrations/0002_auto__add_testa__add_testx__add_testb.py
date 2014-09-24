# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestA'
        db.create_table(u'main_testa', (
            (u'testx_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.TestX'], unique=True, primary_key=True)),
            ('field2', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'main', ['TestA'])

        # Adding model 'TestX'
        db.create_table(u'main_testx', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=7, primary_key=True)),
            ('field0', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'main', ['TestX'])

        # Adding model 'TestB'
        db.create_table(u'main_testb', (
            (u'testx_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.TestX'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'main', ['TestB'])


    def backwards(self, orm):
        # Deleting model 'TestA'
        db.delete_table(u'main_testa')

        # Deleting model 'TestX'
        db.delete_table(u'main_testx')

        # Deleting model 'TestB'
        db.delete_table(u'main_testb')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blog.personalblog': {
            'Meta': {'object_name': 'PersonalBlog'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'disqus': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'twitter_widget_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'main.testa': {
            'Meta': {'object_name': 'TestA', '_ormbases': [u'main.TestX']},
            'field2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'testx_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.TestX']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'main.testb': {
            'Meta': {'object_name': 'TestB', '_ormbases': [u'main.TestX']},
            u'testx_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.TestX']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'main.testx': {
            'Meta': {'object_name': 'TestX'},
            'field0': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True'})
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'blog_wave': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.PersonalBlog']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['main']