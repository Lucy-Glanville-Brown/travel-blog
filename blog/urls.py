from .views import PostCreateView
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]