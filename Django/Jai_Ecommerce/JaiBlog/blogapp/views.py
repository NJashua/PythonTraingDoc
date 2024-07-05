from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializer import BlogSerializer
from .permissions import IsAdminOrReadOnly

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly]

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
