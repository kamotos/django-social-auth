from datetime import datetime
from uuid import uuid4
import urllib

from annoying.decorators import render_to

from django.core.files import File
from django.shortcuts import redirect

from social_auth.forms import UserForm
from social_auth.utils import setting
from social_auth.models import UserSocialAuth
from social_auth.backends import USERNAME
from social_auth.signals import socialauth_registered, \
                                pre_update



def get_username(details, user=None,
                 user_exists=UserSocialAuth.simple_user_exists,
                 *args, **kwargs):
    """Return an username for new user. Return current user username
    if user was given.
    """
    if user:
        return {'username': user.username}

    if details.get(USERNAME):
        username = unicode(details[USERNAME])
    else:
        username = uuid4().get_hex()

    uuid_length = 16
    max_length = UserSocialAuth.username_max_length()
    short_username = username[:max_length - uuid_length]
    final_username = username[:max_length]

    # Generate a unique username for current user using username
    # as base but adding a unique hash at the end. Original
    # username is cut to avoid any field max_length.
    while user_exists(username=final_username):
        username = short_username + uuid4().get_hex()[:uuid_length]
        final_username = username[:max_length]

    return {'username': final_username}


def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """Create user. Depends on get_username pipeline."""
    if user or backend.name not in ('facebook', 'twitter'):
        return {'user': user}
    if not username:
        return None
    # NOTE: not return None because Django raises exception of strip email
    email = kwargs.get('email') or ''
    password = kwargs.get('password')

    user = UserSocialAuth.create_user(username=username, email=email,
                                      password=password)
    user.set_password(password)
    user.save()
    return {
        'user': user,
        'is_new': True
    }


def update_user_details(backend, details, response, user, is_new=False, *args,
                        **kwargs):
    """Update user details using data from provider."""
    if backend.name not in ('twitter', 'facebook'):
        return

    fields_name = backend.RESPONSE_FIELDS
    profile = user.get_profile()

    if not profile.bio and response.get(fields_name['bio'], None):
        profile.bio = response[fields_name['bio']]
    if not profile.user.first_name and response.get('first_name', None):
        user.first_name = response['first_name']
    if not profile.user.last_name and response.get('last_name', None):
        user.last_name = response['last_name']
    if not profile.web and response.get(fields_name['web'], None):
        profile.web = response[fields_name['web']]
    if not profile.image and response.get(fields_name['image'], None):
        content = urllib.urlretrieve(response[fields_name['image']].encode('utf-8'
                                     ).replace("_normal", ""))
        profile.image.save("%s.jpg" % user.id, File(open(content[0])), save=True)
    if not profile.gender and response.get('gender', None):
        profile.gender = response['gender']
    if not profile.birthdate and response.get('birthday', None):
        profile.birthdate = datetime.strptime(response['birthday'],
                                              "%m/%d/%Y").date()
    if not profile.city and response.get('location', None):
        try:
            profile.city = response['location'].get('name', None)
        except AttributeError:
            profile.city = response['location']
        profile.geocode_location()
    profile.save()
    if not is_new:
        return
    return

    changed = False  # flag to track changes
    for name, value in details.iteritems():
        # do not update username, it was already generated
        # do not update configured fields if user already existed
        if name in (USERNAME, 'id', 'pk') or (not is_new and
            name in setting('SOCIAL_AUTH_PROTECTED_USER_FIELDS', [])):
            continue
        if value and value != getattr(user, name, None):
            setattr(user, name, value)
            changed = True


    # user instance (created or retrieved from database), service
    # response and processed details.
    # Fire a pre-update signal sending current backend instance,
    #
    # Also fire socialauth_registered signal for newly registered
    # users.
    #
    # Signal handlers must return True or False to signal instance
    # changes. Send method returns a list of tuples with receiver
    # and it's response.
    signal_response = lambda (receiver, response): response
    signal_kwargs = {'sender': backend.__class__, 'user': user,
                     'response': response, 'details': details}

    changed |= any(filter(signal_response, pre_update.send(**signal_kwargs)))

    # Fire socialauth_registered signal on new user registration
    if is_new:
        changed |= any(filter(signal_response,
                              socialauth_registered.send(**signal_kwargs)))
    if changed:
        user.save()
    profile.save()


def setup(backend, *args, **kwargs):
    user = kwargs.get('user', None)
    setup_session = kwargs['request'].session.pop('socialauth_setup', {})

    if setup_session:
        #If first signing in
        username = setup_session.get('username')
        # NOTE: not return None because Django raises exception of strip email
        email = setup_session.get('email') or ''
        password = setup_session.get('password')

        user = UserSocialAuth.create_user(username=username, email=email,
                                          password=password)
        user.save()
        return {
            'user': user,
            'is_new': True
        }

    if backend.name in ('twitter', 'facebook') and not user:
        return redirect('socialauth_setup')
    else:
        return {'user': user}
#    if user or backend.name not in ('facebook', 'twitter'):
