from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Comment, Post


# copied from code institutde walkthrough project
# I think therefore I blog
class CommentForm(forms.ModelForm):
    """
    inherit from the base form
    """
    class Meta:
        """
        telling the class to use Comment model,
        and display the body field on our form
        """
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ post form """
    class Meta:
        """
        use post as the model, and specify what
        fields to display
        """
        model = Post
        fields = (
            'title',
            'content',
            'excerpt',
            'image',
        )

        widgets = {
            'content': SummernoteWidget(),
            'excerpt': SummernoteWidget(),
        }


class ContactForm(forms.ModelForm):
    """
    contact form for user to
    send messages
    """
    class Meta:
        """
        use Comment as the model, and specify what
        fields to display
        """
        model = Comment
        fields = (
            'name',
            'email',
            'body',
        )
