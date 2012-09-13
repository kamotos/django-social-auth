"""Admin settings"""
from social_auth.utils import setting


if setting('SOCIAL_AUTH_MODELS') in (None, 'social_auth.db.django_models'):
    from django.contrib import admin
    from social_auth.models import UserSocialAuth, Nonce, Association

    class UserSocialAuthOption(admin.ModelAdmin):
        """Social Auth user options"""
        #list_display = ('id', 'username', 'twitter_uid')
        search_fields = ('first_name', 'last_name', 'email',
                'user__username')
        list_select_related = True

    class NonceOption(admin.ModelAdmin):
        """Nonce options"""
        list_display = ('id', 'server_url', 'timestamp', 'salt')
        search_fields = ('server_url',)

    class AssociationOption(admin.ModelAdmin):
        """Association options"""
        list_display = ('id', 'server_url', 'assoc_type')
        list_filter = ('assoc_type',)
        search_fields = ('server_url',)

    admin.site.register(UserSocialAuth, UserSocialAuthOption)
    admin.site.register(Nonce, NonceOption)
    admin.site.register(Association, AssociationOption)
