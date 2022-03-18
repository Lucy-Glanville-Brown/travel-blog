from .views import PostCreateView, PostUpdateView
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]