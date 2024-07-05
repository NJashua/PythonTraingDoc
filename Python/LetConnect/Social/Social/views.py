from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json

from .models import *


def index(request):
    all_posts = Post.objects.all().order_by('-date_created')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    followings = []
    suggestions = []
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
    return render(request, "social/index.html", {
        "posts": posts,
        "suggestions": suggestions,
        "page": "all_posts",
        'profile': False
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "social/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "social/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        profile = request.FILES.get("profile")
        cover = request.FILES.get('cover')
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        
        if password != confirmation:
            return render(request, "social/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.profile_pic = profile if profile else "profile_pic/no_pic.png"
            user.cover = cover
            user.save()
            Follower.objects.create(user=user)
        except IntegrityError:
            return render(request, "social/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "social/register.html")


def profile(request, username):
    user = User.objects.get(username=username)
    all_posts = Post.objects.filter(creater=user).order_by('-date_created')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    followings = []
    suggestions = []
    follower = False
    
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

        if request.user in Follower.objects.get(user=user).followers.all():
            follower = True
    
    follower_count = Follower.objects.get(user=user).followers.all().count()
    following_count = Follower.objects.filter(followers=user).count()
    
    return render(request, 'social/profile.html', {
        "username": user,
        "posts": posts,
        "posts_count": all_posts.count(),
        "suggestions": suggestions,
        "page": "profile",
        "is_follower": follower,
        "follower_count": follower_count,
        "following_count": following_count
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        
        try:
            post = Post.objects.create(creater=request.user, content_text=text, content_image=pic)
            return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("Method must be 'POST'")


@login_required
@csrf_exempt
def edit_post(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        img_chg = request.POST.get('img_change')
        post = Post.objects.get(id=post_id)
        
        try:
            post.content_text = text
            if img_chg != 'false':
                post.content_image = pic
            post.save()
            
            post_text = post.content_text if post.content_text else False
            post_image = post.img_url() if post.content_image else False
            
            return JsonResponse({
                "success": True,
                "text": post_text,
                "picture": post_image
            })
        except Exception as e:
            return JsonResponse({
                "success": False
            })
    else:
        return HttpResponse("Method must be 'POST'")


@csrf_exempt
def like_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            
            try:
                post.likers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def unlike_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            
            try:
                post.likers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def save_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            
            try:
                post.savers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def unsave_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            
            try:
                post.savers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def follow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
            
            try:
                follower, created = Follower.objects.get_or_create(user=user)
                follower.followers.add(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def unfollow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
            
            try:
                follower = Follower.objects.get(user=user)
                follower.followers.remove(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def comment(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            comment = data.get('comment_text')
            post = Post.objects.get(id=post_id)
            
            try:
                newcomment = Comment.objects.create(post=post, commenter=request.user, comment_content=comment)
                post.comment_count += 1
                post.save()
                return JsonResponse([newcomment.serialize()], safe=False, status=201)
            except Exception as e:
                return HttpResponse(e)
    
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post).order_by('-comment_time').all()
        return JsonResponse([comment.serialize() for comment in comments], safe=False)
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def delete_post(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(id=post_id)
            
            if request.user == post.creater:
                try:
                    post.delete()
                    return HttpResponse(status=201)
                except Exception as e:
                    return HttpResponse(e)
            else:
                return HttpResponse(status=404)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))
