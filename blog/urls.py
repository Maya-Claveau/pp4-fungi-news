from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='blogpost_like'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
    path('all_posts', views.AllPosts.as_view(), name='all_posts'),
    path('shared_posts', views.SharedPostsByUsers.as_view(), name='shared_posts'),  # noqa: E501
    path('<slug:slug>/update', views.UpdatePost.as_view(), name='update_post'),  # noqa: E501
    path('<slug:slug>/delete_post', views.DeletePost.as_view(), name='delete_post'),  # noqa: E501
]
