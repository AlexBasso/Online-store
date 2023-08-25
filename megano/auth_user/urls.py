from django.contrib import admin
from django.urls import path, include

from auth_user import views
from auth_user.views import (
    SignInView,
    SignUpView,
    ProfileView,
    ProfileAvatarView,
    ProfilePasswordView,
)

urlpatterns = [
    path("sign-in", SignInView.as_view(), name="login"),
    path("sign-up", SignUpView.as_view(), name="register"),
    path("sign-out", views.signOut),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/avatar", ProfileAvatarView.avatar, name="avatar"),
    path("profile/password", ProfilePasswordView.profile_password, name="password"),
]
