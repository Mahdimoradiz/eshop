from django import forms
from blog.models import BlogComment


class BlogCommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'type': 'text',
            'required': 'required',
        }
    )
    )

    class Meta:
        model = BlogComment
        fields = ["message"]
