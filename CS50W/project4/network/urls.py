from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("profile/<int:profile>", views.profile, name="profile"),
    path("user_profile/<int:profile>", views.user_profile, name="user_profile"),
    path("following", views.following, name="following"),
    path("follow_posts", views.follow_posts, name="follow_posts"),
    path("edit", views.edit, name="edit"),
    path("like", views.like, name="like"),
]
