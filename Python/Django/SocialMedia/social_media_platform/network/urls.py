from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('following/', views.following, name='following'),
    path('saved/', views.saved, name='saved'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('like_post/<int:id>/', views.like_post, name='like_post'),
    path('unlike_post/<int:id>/', views.unlike_post, name='unlike_post'),
    path('save_post/<int:id>/', views.save_post, name='save_post'),
    path('unsave_post/<int:id>/', views.unsave_post, name='unsave_post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]