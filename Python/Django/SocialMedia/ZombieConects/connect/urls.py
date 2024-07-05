# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('settings', views.settings, name='settings'),
#     path('upload', views.upload, name='upload'),
#     path('follow', views.follow, name='follow'),
#     path('search', views.search, name='search'),
#     path('profile/<str:pk>', views.profile, name='profile'),
#     path('like-post', views.like_post, name='like-post'),
#     path('signup', views.signup, name='signup'),
#     path('signin', views.signin, name='signin'),
#     path('logout', views.logout, name='logout'),
# ]

from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),  # Add a trailing slash
    path('upload/', views.upload, name='upload'),  # Add a trailing slash
    path('follow/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
    path('profile/<str:pk>/', views.profile, name='profile'),  # Add a trailing slash
    path('like-post/', views.like_post, name='like-post'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),  # Add a trailing slash
]