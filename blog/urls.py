from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:post_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]

