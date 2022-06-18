from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    use summernote for the blog content
    """
    list_display = ('title', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = ('content', )
    search_fields = ['title', 'content']
