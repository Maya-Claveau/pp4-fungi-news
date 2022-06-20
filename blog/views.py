from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    a post list based on the django generic ListView
    the max number of posts per page is set to 6
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
