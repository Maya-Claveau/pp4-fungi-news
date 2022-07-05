from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='blogpost_like'),
    path('post/add', views.AddPost.as_view(), name='add_post'),
    path('all_posts', views.AllPosts.as_view(), name='all_posts'),
]
