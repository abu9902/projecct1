from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework import permissions
from ..models import Post
from .serializers import MyModelSerializer

class MyModelListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

class MyModelDetialView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

class MyModelCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

class MyModelUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

