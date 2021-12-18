from django.urls import path
from post import views

urlpatterns = [
    path("", views.PostAPIView.as_view(), name="posts-list"),
    path(r"<int:id>/", views.PostUpdateDeleteAPIView.as_view(), name="post-detailed"),
    path(r"<int:id>/upvote/", views.PostUpvoteAPIView.as_view(), name="comments-list"),
    path(r"<int:id>/comments/", views.CommentAPIView.as_view(), name="comments-list"),
]
