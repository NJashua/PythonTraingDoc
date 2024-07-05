from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import *

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    return render(request, 'profile.html', {'user': user, 'posts': posts})

@login_required
def following(request):
    users = request.user.following.all()
    return render(request, 'following.html', {'users': users})

@login_required
def saved(request):
    posts = request.user.saved.all()
    return render(request, 'saved.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        content_text = request.POST['content_text']
        content_image = request.FILES.get('content_image')
        post = Post(creater=request.user, content_text=content_text, content_image=content_image)
        post.save()
        return redirect('index')
    return render(request, 'create_post.html')

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        content_text = request.POST['content_text']
        content_image = request.FILES.get('content_image')
        post.content_text = content_text
        post.content_image = content_image
        post.save()
        return redirect('index')
    return render(request, 'edit_post.html', {'post': post})

@login_required
def like_post(request, id):
    post = Post.objects.get(id=id)
    if request.user in post.likers.all():
        post.likers.remove(request.user)
    else:
        post.likers.add(request.user)
    return JsonResponse({'likes': post.likers.count()})

@login_required
def unlike_post(request, id):
    post = Post.objects.get(id=id)
    post.likers.remove(request.user)
    return JsonResponse({'likes': post.likers.count()})

@login_required
def save_post(request, id):
    post = Post.objects.get(id=id)
    if request.user in post.savers.all():
        post.savers.remove(request.user)
    else:
        post.savers.add(request.user)
    return JsonResponse({'saves': post.savers.count()})

@login_required
def unsave_post(request, id):
    post = Post.objects.get(id=id)
    post.savers.remove(request.user)
    return JsonResponse({'saves': post.savers.count()})

@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return JsonResponse({'followers': user.followers.count()})

@login_required
def unfollow(request, username):
    user = User.objects.get(username=username)
    user.followers.remove(request.user)
    return JsonResponse({'followers': user.followers.count()})

@login_required
def comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        comment_content = request.POST['comment_content']
        comment = Comment(post=post, commenter=request.user, comment_content=comment_content)
        comment.save()
        return redirect('index')
    return render(request, 'comment.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('index')