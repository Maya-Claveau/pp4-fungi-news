from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    use summernote for the blog content,
    and customise the admin panel which showing only
    tile, author, status and created_on. Plus a search field
    on the title and content.
    """
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = ('content', )
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    use modelAdmin to manage the comment section
    """
    list_display = ('name', 'post', 'body', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')

