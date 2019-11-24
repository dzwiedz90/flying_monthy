from django import forms

from comments.models import Comments


class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, required=True)
    author = forms.CharField(max_length=128, required=True)
    meme = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Comments
        fields = ['content', 'author', 'meme']
