from django import forms
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


class ContactForm(forms.Form):
    """
    contact form for user to
    send messages
    """
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def send_email(self):
        """ send email """
        pass
