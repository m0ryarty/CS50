import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from json import dumps
from django.views.generic import ListView

from .models import User, Post, Follow, Like
from django.core.paginator import Paginator


def index(request):

    if request.user.is_authenticated:

        global page_number
        page_number = request.GET.get("page", 1)

        return render(request, "network/index.html", {"user": request.user})

    else:
        return HttpResponseRedirect(reverse("login"))


def posts(request):

    if request.method == "POST":

        post = request.POST["post"]

        if post:
            try:
                new_post = Post(post=post, user=request.user)
                new_post.save()
            except:
                print("Error")

    postList = list(Post.objects.all().values().order_by("-created"))

    list_paginator = Paginator(postList, 10)

    page_obj = list_paginator.get_page(page_number)

    likes = Like.objects.all().values()

    posts = []

    for post in page_obj:

        user = User.objects.filter(id=post["user_id"])[0]
        date = post["created"].strftime(f"%B %d, %Y - %X")
        numberLikes = likes.filter(post=post["id"]).count()
        liked = likes.filter(user=request.user, post=post["id"]).exists()

        post.update(
            {
                "username": user.username,
                "created": date,
                "numberLikes": numberLikes,
                "liked": liked,
                "loggedUser": request.user.id,
            }
        )

        posts.append(post)

    pages = []

    for p in range(list_paginator.num_pages):

        pages.append({"page": p + 1})

    next = list_paginator.page(page_number).has_next()
    previous = list_paginator.page(page_number).has_previous()

    postsData = {
        "posts": posts,
        "paginator": {
            "pages": pages,
            "page": int(page_number),
            "itens": list_paginator.count,
            "next": next,
            "previous": previous,
        },
    }

    return JsonResponse(postsData, safe=False)


def like(request):

    if request.method == "POST":

        like_user = request.POST["likeUser"]
        like_post = request.POST["likePost"]

        user = User(id=like_user)
        post = Post(id=like_post)

        like = Like.objects.filter(user=like_user, post=like_post)

        if like.exists():

            like.delete()
        else:
            new_like = Like(post=post, user=user)
            new_like.save()

    return HttpResponse("index")


@login_required
def profile(request, profile):

    global profile_page
    profile_page = request.GET.get("page", 1)

    follow = Follow.objects.filter(follower=request.user.id).filter(following=profile)

    def followUser(id):
        return User.objects.filter(id=id).first()

    if request.method == "POST":
        if request.user.id != profile:
            if follow.exists():
                follow.delete()

            else:
                Follow.objects.create(
                    follower=followUser(request.user.id), following=followUser(profile)
                )

    user = User.objects.filter(id=profile)

    profile_data = {
        "userId": request.user.id,
        "username": user[0].username,
        "profile": profile,
        "follow": follow.exists(),
    }

    return render(
        request, "network/profile.html", {"profile_data": json.dumps(profile_data)}
    )


@login_required
def user_profile(request, profile):

    postList = list(Post.objects.filter(user=profile).values().order_by("-created"))

    list_paginator = Paginator(postList, 10)

    page_obj = list_paginator.get_page(profile_page)

    likes = Like.objects.all().values()

    posts = []
    for post in page_obj:
        user = User.objects.filter(id=post["user_id"])[0]
        date = post["created"].strftime(f"%B %d, %Y - %X")
        numberLikes = likes.filter(post=post["id"]).count()
        liked = likes.filter(user=request.user, post=post["id"]).exists()
        post.update(
            {
                "username": user.username,
                "created": date,
                "numberLikes": numberLikes,
                "liked": liked,
                "loggedUser": request.user.id,
            }
        )
        posts.append(post)

    pages = []

    for p in range(list_paginator.num_pages):

        pages.append({"page": p + 1})

    next = list_paginator.page(profile_page).has_next()
    previous = list_paginator.page(profile_page).has_previous()

    data = {
        "follow": {
            "follower": Follow.objects.filter(following=request.user).count(),
            "following": Follow.objects.filter(follower=request.user).count(),
        },
        "paginator": {
            "pages": pages,
            "page": int(profile_page),
            "itens": list_paginator.count,
            "next": next,
            "previous": previous,
        },
        "profileData": posts,
    }

    return JsonResponse(data, safe=False)


@login_required
def following(request):

    if request.user.is_authenticated:

        global follow_page
        follow_page = request.GET.get("page", 1)

        return render(request, "network/following.html", {"user": request.user})

    else:
        return HttpResponseRedirect(reverse("login"))


def follow_posts(request):
    following_users = Follow.objects.filter(follower=request.user)

    post_list = []
    for p in following_users:
        posts = list(Post.objects.filter(user=p.following).values())
        post_list += posts

    list_paginator = Paginator(
        sorted(post_list, key=lambda x: x["created"], reverse=True), 10
    )

    page_obj = list_paginator.get_page(follow_page)

    likes = Like.objects.all().values()

    posts = []

    for post in page_obj:

        user = User.objects.filter(id=post["user_id"])[0]
        date = post["created"].strftime(f"%B %d, %Y - %X")
        numberLikes = likes.filter(post=post["id"]).count()
        liked = likes.filter(user=request.user, post=post["id"]).exists()

        post.update(
            {
                "username": user.username,
                "created": date,
                "numberLikes": numberLikes,
                "liked": liked,
                "loggedUser": request.user.id,
            }
        )

        posts.append(post)

    pages = []

    for p in range(list_paginator.num_pages):

        pages.append({"page": p + 1})

    next = list_paginator.page(follow_page).has_next()
    previous = list_paginator.page(follow_page).has_previous()

    postsData = {
        "posts": posts,
        "paginator": {
            "pages": pages,
            "page": int(follow_page),
            "itens": list_paginator.count,
            "next": next,
            "previous": previous,
        },
    }

    return JsonResponse(postsData, safe=False)


def edit(request):
    if request.method == "POST":

        edited_post = request.POST["edit"]
        postId = request.POST["postId"]

        new_post = Post(id=postId, user=request.user)
        new_post.post = edited_post
        new_post.save()

    postList = list(Post.objects.all().values().order_by("-created"))

    list_paginator = Paginator(postList, 10)

    page_obj = list_paginator.get_page(page_number)

    likes = Like.objects.all().values()

    posts = []

    for post in page_obj:

        user = User.objects.filter(id=post["user_id"])[0]
        date = post["created"].strftime(f"%B %d, %Y - %X")
        numberLikes = likes.filter(post=post["id"]).count()
        liked = likes.filter(user=request.user, post=post["id"]).exists()

        post.update(
            {
                "username": user.username,
                "created": date,
                "numberLikes": numberLikes,
                "liked": liked,
                "loggedUser": request.user.id,
            }
        )

        posts.append(post)

    return JsonResponse(posts, safe=False)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
