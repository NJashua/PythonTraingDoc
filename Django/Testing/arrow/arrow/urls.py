from django.urls import path
# import Testing
# import Testing.views
from travello import views
urlpatterns = [
    # path('home/add/',Testing.views.add, name='add'),
    path('travello/', views.travello, name='travello')
]
