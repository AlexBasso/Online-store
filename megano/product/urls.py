from django.urls import path

from product.views import ProductView, ProductReviewsView

urlpatterns = [
    path("product/<int:id>", ProductView.as_view(), name="product"),
    path(
        "product/<int:id>/reviews", ProductReviewsView.as_view(), name="product_review"
    ),
    # path("sign-in", SignInView.as_view(), name="login"),
    # path("sign-up", SignUpView.as_view(), name="register"),
    # path("sign-out", views.signOut),
    # path("profile", ProfileView.as_view(), name="profile"),
    # path("profile/avatar", ProfileAvatarView.avatar, name="avatar"),
    # path("profile/password", ProfilePasswordView.profile_password, name="password"),
]
