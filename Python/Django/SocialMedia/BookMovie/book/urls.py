# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('api/movies/', views.api_movies, name='api_movies'),
#     path('book_movie/<int:movie_id>/', views.book_movie, name='book_movie'),
#     path('book_show/<int:show_id>/', views.book_show, name='book_show'),
#     path('login/', views.login_page, name='login'),
#     path('register/', views.register, name='register'),
#     path('logout/', views.custom_logout, name='logout'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/movies/', views.api_movies, name='api_movies'),
    path('book/<int:movie_id>/', views.book_movie, name='book_movie'),
    path('book/show/<int:show_id>/', views.book_show, name='book_show'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
]