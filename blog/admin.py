from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    use summernote for the blog content
    """
    summernote_fields = ('content')
