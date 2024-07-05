from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_api.urls')),  # Include the urls of your todo_api app here
]
