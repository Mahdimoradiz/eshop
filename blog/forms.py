from django import forms
from blog.models import BlogComment

class BlogCommentForm(forms.ModelForm):
      class Meta:
            model = BlogComment
            fields = "__all__"
            
            
      name = forms.CharField(widget=forms.TextInput(
            attrs={
                  'type': 'text',
                  'required': 'required',
                  }
            )
      )
      email = forms.CharField(widget=forms.EmailInput(
            attrs={
                  'type': 'email',
                  'required': 'required',
                  }
            )
      )
      message = forms.CharField(widget=forms.TextInput(
            attrs={
                  'type': 'text',
                  'required': 'required',
                  }
            )
      )
      