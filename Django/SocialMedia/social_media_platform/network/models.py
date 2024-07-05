from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/')
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True)
    groups = models.ManyToManyField(Group, related_name='network_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='network_user_permissions')
    def __str__(self):
        return self.username
 
class Post(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date_created = models.DateTimeField(default=timezone.now)
    content_text = models.TextField(max_length=140, blank=True)
    content_image = models.ImageField(upload_to='posts/', blank=True)
    likers = models.ManyToManyField(User,blank=True , related_name='likes')
    savers = models.ManyToManyField(User,blank=True , related_name='saved')
    comment_count = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenters')
    comment_content = models.TextField(max_length=90)
    comment_time = models.DateTimeField(default=timezone.now)

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')