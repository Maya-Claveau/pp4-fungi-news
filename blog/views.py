from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Post
from .forms import CommentForm, PostForm


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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
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

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
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


class AddPost(View):
    """allow user to add a post"""

    def get(self, request):
        """to get add_post.html"""

        context = {'form': PostForm()}
        return render(request, 'add_post.html', context)

    def post(self, request):
        """
        to allow user to post new articles to
        the blog for others to see and interact with
        """

        # form = PostForm(request.POST)
        # title = form.instance.title
        # if Post.objects.filter(
        #     Q(title=title)
        # ).exists():
        #     messages.error(
        #         request,
        #         'Post Title already exists, please try another one.'
        #     )
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = NameForm()

        context = {'form': form}
        return render(request, 'post_detail.html', context)




            # form = PostForm(get)
            # form = PostForm(request.POST, instance=title)
            # if form.is_valid():
            #     form.save()
            #     messages.success(request, 'Thank you for sharing your post.')
            #     return redirect('/')
