from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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


class PostDetail(View):
    """
    this part of the code is copied from code institude walkthrough
    'I think therefore I blog'. The purpose is to render the post
    detail according to their unique title, and also if user is logged
    in, they can like the post as well as comments.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        to render the post detail according
        to their unique title, and also if user is logged
        in, they can like the post as well as comments
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            },
        )


class PostLike(View):
    """
    this is also part of code institude walkthrough
    'I think therefore I blog'.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        handle the like button from user, if already liked
        it will remove the like, otherwise when click it will
        like the post
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
