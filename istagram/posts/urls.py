from django.urls import path

from .views import CreatePostView, ListPostView

urlpatterns = [
    path("", ListPostView.as_view(), name="list_post"),
    path("new/", CreatePostView.as_view(), name="new_post")
]