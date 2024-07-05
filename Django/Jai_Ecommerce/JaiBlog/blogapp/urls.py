from django.urls import path
from .views import BlogListCreate, BlogDetail
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('api-token-auth/', obtain_auth_token),
]
