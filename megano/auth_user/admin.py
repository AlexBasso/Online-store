from django.contrib import admin

from auth_user.models import Profile, Avatar

admin.site.register(Avatar)
admin.site.register(Profile)
