from django.urls import path

from tag.views import TagView

urlpatterns = [
    path("tags", TagView.as_view(), name="tags"),
]
