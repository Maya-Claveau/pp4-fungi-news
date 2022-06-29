from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    store the Post data
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        order the post on the created_on field in the decending order
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        return a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        total number of likes on a post
        """
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    """
    store data for comment
    """

    name = models.CharField(max_length=70)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """
        order the comments on the created_on field in the ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        return a string of the comment made by the user
        """
        return f"Comment {self.body} by {self.name}"
