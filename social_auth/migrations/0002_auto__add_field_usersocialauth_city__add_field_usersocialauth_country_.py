# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserSocialAuth.city'
        db.add_column('social_auth_usersocialauth', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.country'
        db.add_column('social_auth_usersocialauth', 'country',
                      self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.state'
        db.add_column('social_auth_usersocialauth', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.gender'
        db.add_column('social_auth_usersocialauth', 'gender',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.birthdate'
        db.add_column('social_auth_usersocialauth', 'birthdate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.web'
        db.add_column('social_auth_usersocialauth', 'web',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.bio'
        db.add_column('social_auth_usersocialauth', 'bio',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.image'
        db.add_column('social_auth_usersocialauth', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.cta_notification'
        db.add_column('social_auth_usersocialauth', 'cta_notification',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserSocialAuth.badge_notification'
        db.add_column('social_auth_usersocialauth', 'badge_notification',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserSocialAuth.socialiq_notification'
        db.add_column('social_auth_usersocialauth', 'socialiq_notification',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserSocialAuth.level'
        db.add_column('social_auth_usersocialauth', 'level',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.update_date'
        db.add_column('social_auth_usersocialauth', 'update_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 9, 5, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.quantile'
        db.add_column('social_auth_usersocialauth', 'quantile',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'UserSocialAuth.is_partial'
        db.add_column('social_auth_usersocialauth', 'is_partial',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.twitter_handle'
        db.add_column('social_auth_usersocialauth', 'twitter_handle',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.social_sharing'
        db.add_column('social_auth_usersocialauth', 'social_sharing',
                      self.gf('jsonfield.fields.JSONField')(default=None, max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.valid_tokens'
        db.add_column('social_auth_usersocialauth', 'valid_tokens',
                      self.gf('jsonfield.fields.JSONField')(default={}, max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserSocialAuth.socialiq_score'
        db.add_column('social_auth_usersocialauth', 'socialiq_score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.trust_score'
        db.add_column('social_auth_usersocialauth', 'trust_score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.network_score'
        db.add_column('social_auth_usersocialauth', 'network_score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.facebook_score'
        db.add_column('social_auth_usersocialauth', 'facebook_score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.twitter_score'
        db.add_column('social_auth_usersocialauth', 'twitter_score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.facebook_friends'
        db.add_column('social_auth_usersocialauth', 'facebook_friends',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.twitter_followers'
        db.add_column('social_auth_usersocialauth', 'twitter_followers',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.twitter_avg_mentions'
        db.add_column('social_auth_usersocialauth', 'twitter_avg_mentions',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.twitter_avg_retweets'
        db.add_column('social_auth_usersocialauth', 'twitter_avg_retweets',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.tweets_count'
        db.add_column('social_auth_usersocialauth', 'tweets_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.facebook_avg_likes'
        db.add_column('social_auth_usersocialauth', 'facebook_avg_likes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.facebook_avg_comments'
        db.add_column('social_auth_usersocialauth', 'facebook_avg_comments',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UserSocialAuth.facebook_avg_posts'
        db.add_column('social_auth_usersocialauth', 'facebook_avg_posts',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserSocialAuth.city'
        db.delete_column('social_auth_usersocialauth', 'city')

        # Deleting field 'UserSocialAuth.country'
        db.delete_column('social_auth_usersocialauth', 'country')

        # Deleting field 'UserSocialAuth.state'
        db.delete_column('social_auth_usersocialauth', 'state')

        # Deleting field 'UserSocialAuth.gender'
        db.delete_column('social_auth_usersocialauth', 'gender')

        # Deleting field 'UserSocialAuth.birthdate'
        db.delete_column('social_auth_usersocialauth', 'birthdate')

        # Deleting field 'UserSocialAuth.web'
        db.delete_column('social_auth_usersocialauth', 'web')

        # Deleting field 'UserSocialAuth.bio'
        db.delete_column('social_auth_usersocialauth', 'bio')

        # Deleting field 'UserSocialAuth.image'
        db.delete_column('social_auth_usersocialauth', 'image')

        # Deleting field 'UserSocialAuth.cta_notification'
        db.delete_column('social_auth_usersocialauth', 'cta_notification')

        # Deleting field 'UserSocialAuth.badge_notification'
        db.delete_column('social_auth_usersocialauth', 'badge_notification')

        # Deleting field 'UserSocialAuth.socialiq_notification'
        db.delete_column('social_auth_usersocialauth', 'socialiq_notification')

        # Deleting field 'UserSocialAuth.level'
        db.delete_column('social_auth_usersocialauth', 'level')

        # Deleting field 'UserSocialAuth.update_date'
        db.delete_column('social_auth_usersocialauth', 'update_date')

        # Deleting field 'UserSocialAuth.quantile'
        db.delete_column('social_auth_usersocialauth', 'quantile')

        # Deleting field 'UserSocialAuth.is_partial'
        db.delete_column('social_auth_usersocialauth', 'is_partial')

        # Deleting field 'UserSocialAuth.twitter_handle'
        db.delete_column('social_auth_usersocialauth', 'twitter_handle')

        # Deleting field 'UserSocialAuth.social_sharing'
        db.delete_column('social_auth_usersocialauth', 'social_sharing')

        # Deleting field 'UserSocialAuth.valid_tokens'
        db.delete_column('social_auth_usersocialauth', 'valid_tokens')

        # Deleting field 'UserSocialAuth.socialiq_score'
        db.delete_column('social_auth_usersocialauth', 'socialiq_score')

        # Deleting field 'UserSocialAuth.trust_score'
        db.delete_column('social_auth_usersocialauth', 'trust_score')

        # Deleting field 'UserSocialAuth.network_score'
        db.delete_column('social_auth_usersocialauth', 'network_score')

        # Deleting field 'UserSocialAuth.facebook_score'
        db.delete_column('social_auth_usersocialauth', 'facebook_score')

        # Deleting field 'UserSocialAuth.twitter_score'
        db.delete_column('social_auth_usersocialauth', 'twitter_score')

        # Deleting field 'UserSocialAuth.facebook_friends'
        db.delete_column('social_auth_usersocialauth', 'facebook_friends')

        # Deleting field 'UserSocialAuth.twitter_followers'
        db.delete_column('social_auth_usersocialauth', 'twitter_followers')

        # Deleting field 'UserSocialAuth.twitter_avg_mentions'
        db.delete_column('social_auth_usersocialauth', 'twitter_avg_mentions')

        # Deleting field 'UserSocialAuth.twitter_avg_retweets'
        db.delete_column('social_auth_usersocialauth', 'twitter_avg_retweets')

        # Deleting field 'UserSocialAuth.tweets_count'
        db.delete_column('social_auth_usersocialauth', 'tweets_count')

        # Deleting field 'UserSocialAuth.facebook_avg_likes'
        db.delete_column('social_auth_usersocialauth', 'facebook_avg_likes')

        # Deleting field 'UserSocialAuth.facebook_avg_comments'
        db.delete_column('social_auth_usersocialauth', 'facebook_avg_comments')

        # Deleting field 'UserSocialAuth.facebook_avg_posts'
        db.delete_column('social_auth_usersocialauth', 'facebook_avg_posts')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'social_auth.association': {
            'Meta': {'object_name': 'Association'},
            'assoc_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued': ('django.db.models.fields.IntegerField', [], {}),
            'lifetime': ('django.db.models.fields.IntegerField', [], {}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'server_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'social_auth.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'server_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'social_auth.usersocialauth': {
            'Meta': {'object_name': 'UserSocialAuth'},
            'badge_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cta_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook_avg_comments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook_avg_likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook_avg_posts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook_friends': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_partial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'network_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'quantile': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'social_sharing': ('jsonfield.fields.JSONField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'socialiq_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'socialiq_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trust_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tweets_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter_avg_mentions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter_avg_retweets': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter_extra_data': ('social_auth.fields.JSONField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            'twitter_followers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'twitter_uid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'social_auth'", 'to': "orm['auth.User']"}),
            'valid_tokens': ('jsonfield.fields.JSONField', [], {'default': '{}', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['social_auth']