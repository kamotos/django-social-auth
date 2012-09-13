"""Django ORM models for Social Auth"""
from django.contrib.auth.models import User
from django.db import models
from django.db.utils import IntegrityError

from social_auth.db.base import UserSocialAuthMixin, AssociationMixin, \
                                NonceMixin
from social_auth.fields import JSONField
from social_auth.utils import setting


# If User class is overridden, it *must* provide the following fields
# and methods work with django-social-auth:
#
#   username   = CharField()
#   last_login = DateTimeField()
#   is_active  = BooleanField()
#   def is_authenticated():
#       ...
if setting('SOCIAL_AUTH_USER_MODEL'):
    UserModel = models.get_model(*setting('SOCIAL_AUTH_USER_MODEL')
                                    .rsplit('.', 1))
else:
    from django.contrib.auth.models import User as UserModel
from profile.models import Profile

class UserSocialAuth(Profile, UserSocialAuthMixin):
    """Social Auth association model"""
    User = UserModel
    user = models.OneToOneField(UserModel, related_name='social_auth')
    #provider = models.CharField(max_length=32)
    #uid = models.CharField(max_length=255)
    #extra_data = JSON
    #
    #
    # Field(default='{}')
    twitter_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    twitter_extra_data = JSONField(default='{}', null=True, blank=True)
    twitter_access_token = models.CharField(max_length=255, null=True, blank=True)

    foursquare_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    foursquare_extra_data = JSONField(default='{}', null=True, blank=True)
    foursquare_access_token = models.CharField(max_length=255, null=True, blank=True)

    facebook_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    facebook_extra_data = JSONField(default='{}', null=True, blank=True)
    facebook_access_token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """Meta data"""
        app_label = 'social_auth'

    @classmethod
    def create_user(cls, *args, **kwargs):
        return cls.User.objects.create_user(*args, **kwargs)

    @classmethod
    def get_social_auth(cls, provider, uid):
        q_kwargs = {"{0}_id".format(provider): uid}
        try:
            return cls.objects.get(**q_kwargs)
        except UserSocialAuth.DoesNotExist:
            return None

    @classmethod
    def username_max_length(cls):
        return cls.User._meta.get_field('username').max_length


class Nonce(models.Model, NonceMixin):
    """One use numbers"""
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)

    class Meta:
        app_label = 'social_auth'


class Association(models.Model, AssociationMixin):
    """OpenId account association"""
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)  # Stored base64 encoded
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        app_label = 'social_auth'


def is_integrity_error(exc):
    return exc.__class__ is IntegrityError

Profile = UserSocialAuth