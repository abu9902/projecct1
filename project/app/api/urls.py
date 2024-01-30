from django.urls import path
from .views import MyModelListCreateView, MyModelDetialView, MyModelCreateView, MyModelUpdateView

urlpatterns = [
    path('api/posts/', MyModelListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', MyModelDetialView.as_view(), name='post-detail'),
    path('api/posts/create/', MyModelCreateView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/update/', MyModelUpdateView.as_view(), name='post-update'),

]
